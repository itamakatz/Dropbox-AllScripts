import re
import sys
import time
import msvcrt
from os import remove
from shutil import move
from os.path import join, isfile

def wait_input_to_exit():
    msvcrt.getch()

RUN = False;
CHANGE_PRINTING_SPEED = False;

# =================================================================================== #
# ================================== USER INPUT ===================================== #
# =================================================================================== #

# Enter path to the G-Code file and file name itself
PATH = r"H:\Dropbox\Coding & Tools\3D Printer & Robotics\STL & G-Code Files\Current Prints\Owl_Pen_Holder\Owl_Pen_Holder___Tools_Holder";
# PATH = r"J:\Dropbox\Coding & Tools\3D Printer & Robotics\STL & G-Code Files\Calibration Parts\Stringing Test\Ultrafast_and_economical_stringing_test\files";
	
FILE = "\\" + r"owl-Pen_Holder-support - v3";

# PATH = input("Please Enter File Path:\n");
# print();
# FILE = "\\" + input("Please Enter File Name:\n");

# print("You Entered:");
# print(PATH);
# print(FILE);
# print();

# Special fan speed for a particular layer such as the 2nd layer regardless of the modular change 
LAYER_SPECIAL_CASE = 1; # Numer of layer with the special speed
FAN_SPECIAL_CASE_PERCENTAGE = 0; # value of the desired speed

# Set fan settings
# For 2.5mm nuzzle - LAYER_BEGING = 10, LEYER_STEP = 3, FAN_STEP = 4, FAN_MIN_PERCENTAGE = 10, FAN_MAX_PERCENTAGE = 85
LAYER_BEGING = 2; # 3; # 5; # 10; # 5; # 2; # First layer on which the fan will be turned on. Must be grater or equal to 1
LEYER_STEP = 1; # 2; # 3; # 1; # Number of layers between a change in fan speed 
FAN_STEP = 4; # 6; # 8; # Incremental value of the fan's speed after each change
FAN_MIN_PERCENTAGE = 15; # 10; # 30; # Initial fan speed on layer numer LAYER_BEGING
FAN_MAX_PERCENTAGE = 50; # 50; # 100; # 80; # The max speed at which the fan can run (Higher than 127PWM ~ 50% results in stringing)

# Run fan in full power befor setting speed in case of a stalling fan. Set True one or none of the following
BLIP_TIME = False; # Stall between the full fan speed to the target speed is only based on time
BLIP_LINES = True; # Stall between the full fan speed to the target speed is NOT based on time but rather lines of code

# Blip parameters (upon change in fan speed, increase to 100% and the lower to the target)
BLIP_STALL_TIME = 500; # Time in milliseconds
BLIP_STALL_LINES = 1; # Number of G-code lines between max speed and target speed
BLIP_THRESHOLDS_PERCENTAGE = 25; # Porcentage threshold from which blip shold be disabled

# Print speed parameters
LAYER_SPEED_PAIRS = [(1, 100)];
# LAYER_SPEED_PAIRS = [(1, 50), (5, 100)];
# LAYER_SPEED_PAIRS = [(1, 100), (9, 220)];
# LAYER_SPEED_PAIRS = [(1, 200)];
# LAYER_SPEED_PAIRS = [(1, 75), (9, 100)];

# =================================== Turn Script On ================================ #

RUN = True;
# CHANGE_PRINTING_SPEED = True;

# =================================================================================== #

if ".gcode" not in FILE : FILE += ".gcode" 

MODIFIED_STATUS = "Created by Modular_Fan.py script. Itamar Katz."
STATUS_ON_FILE = MODIFIED_STATUS + "\n";
STARTING_LINE_FLAG = "; " + STATUS_ON_FILE

fan_max_speed = int(round(FAN_MAX_PERCENTAGE * 255 / 100));
fan_min_speed = int(round(FAN_MIN_PERCENTAGE * 255 / 100));

blip_threshold_speed = int(round(BLIP_THRESHOLDS_PERCENTAGE * 255 / 100));

layer_count = 0;
blip_lines_count = 0;
fan_current_speed = 0;
fan_current_speed_for_blip_line = 0;

# regex to find layer count and G1 / G2 lines
layer_reg = re.compile("; layer \d");
g1_g2_commands = re.compile("G[1\2]");

# ======================================= #
# Safty check before messing with the files
# ======================================= #

if RUN == False:
	print("***************************************");
	print("============= Can't Run ===============");
	print("***************************************\n");

	print("Please set RUN to True");

	print("\nPlease press any key to exit");
	wait_input_to_exit();
	sys.exit();

# ======================================= #

tmp_file = open("".join([PATH, FILE, "tmp"]), 'w+');

if not isfile("".join([PATH, FILE])):
	print("***********************************");
	print("============= ERROR ===============");
	print("***********************************\n");

	print("Error! File Does Not Exist");

	wait_input_to_exit();
	sys.exit();

with open("".join([PATH, FILE]), 'r') as f:

	if len(f.read(1)) == 0:	
		print("***********************************");
		print("============= ERROR ===============");
		print("***********************************\n");

		print("Error! File is empty");

		wait_input_to_exit();
		sys.exit();

	f.seek(0)
	first_line = f.readline()

	if(first_line == STARTING_LINE_FLAG):
		print("***********************************");
		print("============= ERROR ===============");
		print("***********************************\n");

		print("Error! File has already been modified thus can't run script on the file again.");

		wait_input_to_exit();
		sys.exit();
	else:
		tmp_file.write(STARTING_LINE_FLAG);

f = open("".join([PATH, FILE]), "r")

for line in f:

	tmp_file.write(line);

	# == BLIP LINES control == #

	if blip_lines_count != 0:

		# exclude non G1 or G2 moves from the count
		if g1_g2_commands.match(line):
			blip_lines_count += 1;

		if blip_lines_count == BLIP_STALL_LINES + 1:
			tmp_file.write("M106 S" + str(fan_current_speed_for_blip_line) + " ; Set Fan Speed. " + STATUS_ON_FILE);
			blip_lines_count = 0;



	if layer_reg.match(line):

		layer_count += 1;

		if (layer_count >= LAYER_BEGING) and ((layer_count - LAYER_BEGING) % LEYER_STEP == 0) and (fan_current_speed < fan_max_speed):

			if fan_current_speed == 0:
				fan_current_speed = fan_min_speed;
			else:
				fan_current_speed += FAN_STEP;

			if fan_current_speed > fan_max_speed:
				fan_current_speed = fan_max_speed;

			print("Im in: Layer numer - " + str(layer_count) + ".\n   Fan Speed - " + \
				str(int(round(fan_current_speed * 100 / 255))) + "%");

			# == BLIP control == #

			if fan_current_speed >= blip_threshold_speed or not (BLIP_TIME or BLIP_LINES):
				tmp_file.write("M106 S" + str(fan_current_speed) + " ; Set Fan Speed. " + STATUS_ON_FILE);

			elif BLIP_TIME:
				tmp_file.write("M106 S255" + " ; " + STATUS_ON_FILE);
				tmp_file.write("G4 P" + str(BLIP_STALL_TIME) + " ; Stall Machine (milliseconds). " + STATUS_ON_FILE);
				tmp_file.write("M106 S" + str(fan_current_speed) + " ; Set Fan Speed. " + STATUS_ON_FILE);

			elif BLIP_LINES:
				tmp_file.write("M106 S255" + " ; Set Fan Speed. " + STATUS_ON_FILE);
				blip_lines_count = 1;
				fan_current_speed_for_blip_line = fan_current_speed;

		elif layer_count == LAYER_SPECIAL_CASE:

			# == BLIP control == #
			
			fans_special_case_speed = int(round(FAN_SPECIAL_CASE_PERCENTAGE * 255 / 100));
			
			print("Im in: Layer numer - " + str(layer_count) + ".\n   Fan Speed - " + \
				str(int(round(fans_special_case_speed * 100 / 255))) + "%");

			if not (BLIP_TIME or BLIP_LINES):
				tmp_file.write("M106 S" + str(fans_special_case_speed) + " ; Set Fan Speed. " + STATUS_ON_FILE);

			elif BLIP_TIME:
				tmp_file.write("M106 S255" + " ; Set Fan Speed. " + STATUS_ON_FILE);
				tmp_file.write("G4 P" + str(BLIP_STALL_TIME) + " ; Stall Machine (milliseconds). " + STATUS_ON_FILE);
				tmp_file.write("M106 S" + str(fans_special_case_speed) + " ; Set Fan Speed. " + STATUS_ON_FILE);

			elif BLIP_LINES:
				tmp_file.write("M106 S255" + " ; Set Fan Speed. " + STATUS_ON_FILE);
				blip_lines_count = 1;	
				fan_current_speed_for_blip_line = fans_special_case_speed;

		if CHANGE_PRINTING_SPEED:
			for (layer, speed) in LAYER_SPEED_PAIRS:
				if layer == layer_count:
					tmp_file.write("M220 S" + str(speed) + " ; Set Printing Speed. " + STATUS_ON_FILE);


tmp_file.truncate();
tmp_file.close();

f.close();

remove("".join([PATH, FILE]));
move("".join([PATH, FILE, "tmp"]), "".join([PATH, FILE]));

print_values = [LEYER_STEP, FAN_STEP, fan_max_speed, fan_min_speed, fan_current_speed, layer_count, blip_threshold_speed];
print_variable_names = ["LEYER_STEP", "FAN_STEP", "fan_max_speed", "fan_min_speed", "fan_current_speed", "layer_count", "blip_threshold_speed"];

print("\n" + "\n".join([m + " - " + n for m,n in zip(print_variable_names, map(str, print_values))]));


print("\nPlease press any key to exit");
wait_input_to_exit();
