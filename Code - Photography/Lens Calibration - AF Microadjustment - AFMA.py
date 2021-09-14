import os
import math
import errno
import msvcrt
import os.path
import itertools
from os import listdir
from os.path import isfile, join

RUN = False
# micro_adjustment_list = ["+1", "+2", "+3", "+4", "+5"]
# micro_adjustment_list = ["-6", "-5", "-4", "-3", "-2", "-1", "+0"]
# micro_adjustment_list = ["-11", "-10", "-9", "-8", "-7"]
micro_adjustment_list = ["-6", "-5", "-4", "-3", "-2", "-1", "+0", "-11", "-10", "-9", "-8", "-7", "+1", "+2", "+3", "+4", "+5"]
# order_list = 			[5, 6, 7, 8, 9, 10, 11, 0, 1, 2, 3, 4, 12, 13, 14, 15, 16]

def check_dir_exists(path):
	try:
		os.makedirs(path)
	except OSError as exception:
		if exception.errno != errno.EEXIST:
			raise

# given a path reame all the files inside
def rename_method(PATH):
	os.chdir(PATH);

	# find all files in the directory
	only_files = [file for file in listdir(PATH) if isfile(join(PATH,file)) and file.endswith(".JPG")];
	only_files = sorted(only_files);

	check_dir_exists(PATH + "\\Infinity");
	check_dir_exists(PATH + "\\After Infinity");
	check_dir_exists(PATH + "\\MFD");
	check_dir_exists(PATH + "\\After MFD");

	for i in range(0, len(only_files)):
		
		sub_folder = "";

		if (i % 8 == 0 or i % 8 == 1):
			sub_folder = "\\Infinity\\";
		elif (i % 8 == 2 or i % 8 == 3):
			sub_folder = "\\After Infinity\\";
		elif (i % 8 == 4 or i % 8 == 5):
			sub_folder = "\\MFD\\";
		elif (i % 8 == 6 or i % 8 == 7):
			sub_folder = "\\After MFD\\";

		os.rename(PATH + "\\" + only_files[i], PATH + sub_folder + str(i//8*2 + i%2) + " - " + micro_adjustment_list[i//8] + "_" + str(i%2 + 1) + ".JPG");
		# os.rename(PATH + "\\" + only_files[i], PATH + sub_folder + str(order_list[i//8]*2 + i%2) + " - " + micro_adjustment_list[i//8] + "_" + str(i%2 + 1) + ".JPG");
		

def wait_input_to_exit():
	msvcrt.getch()


# -------- edit path -------- #
path = r"C:\Users\Itamar\Desktop\Lens Calibration\100-400mm\400mm\-11, 5, 1"

# -------- safty net - Uncomment to run -------- #
# RUN = True


def run(path):
	try:
		rename_method(path);
		print ("Done Running - " + path);
	except Exception as e: 
		print("An exception was thrown:");
		print(e);
	return;

print("Starting Program\n");

if RUN == True:
	run(path);
	print("Program has Finished Correctly");
else:
	print("Program did not run. RUN = False");

print("\nPlease press any key to exit");
wait_input_to_exit();


