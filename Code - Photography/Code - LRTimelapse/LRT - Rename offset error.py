import os
import math
import string
import random
import msvcrt
import os.path
from os import listdir
from time import sleep
from os.path import isfile, join

RUN = False;
PRINT_PROGRESS = True;
g_ITER_COUNT = 0;
g_PROGRESS_COUNTER = 0;
SUFFIX_STR = ''.join(random.choices(string.ascii_uppercase, k=5));

# set the offset of the sequence do to a different export
OFFSET_AMOUNT = 0;

def print_process(demuninator):
	global g_ITER_COUNT, g_PROGRESS_COUNTER;

	if PRINT_PROGRESS == True and math.floor(g_ITER_COUNT / demuninator) == g_PROGRESS_COUNTER + 1:
		g_PROGRESS_COUNTER += 1;
		print("\tDone " + str(g_PROGRESS_COUNTER * 10) + "%")			
	
	g_ITER_COUNT += 1;

# given a path reame all the files inside
def rename_method(PATH):
	os.chdir(PATH);

	# find all files in the directory
	only_files = [file for file in listdir(PATH) if isfile(join(PATH,file))];

	global g_ITER_COUNT, g_PROGRESS_COUNTER;

	g_ITER_COUNT = 0;
	g_PROGRESS_COUNTER = 0;

	demuninator = math.floor(len(only_files)/10);
	if demuninator == 0: 
		global PRINT_PROGRESS;
		PRINT_PROGRESS = False; 
	
	# to ensure no file is renamed to an existing filename, check if there could 
	# be overlaping. If so rename files with arbitrary suffix
	if len(only_files) < OFFSET_AMOUNT:

		print("Renaming files with arbitrary suffix:")

		for file in only_files:
			print_process(demuninator);

			filename, file_extension = os.path.splitext(file);

			os.rename(file, filename + "_suffix_" + SUFFIX_STR + file_extension);

	# since files were renamed, reinitialize the array
	only_files = [file for file in listdir(PATH) if isfile(join(PATH,file))];

	g_ITER_COUNT = 0;
	g_PROGRESS_COUNTER = 0;

	print("Adjusting file name as needed:")

	for file in only_files:

		print_process(demuninator);

		filename, file_extension = os.path.splitext(file);

		# cases to retain the syntax 
		if int(filename[4:9]) < 10:
			os.rename(file, "LRT_0000" + str(int(filename[4:9]) + OFFSET_AMOUNT) + file_extension);
		
		elif int(filename[4:9]) < 100:
			os.rename(file, "LRT_000" + str(int(filename[4:9]) + OFFSET_AMOUNT) + file_extension);
		
		elif int(filename[4:9]) < 1000:
			os.rename(file, "LRT_00" + str(int(filename[4:9]) + OFFSET_AMOUNT) + file_extension);

		elif int(filename[4:9]) < 10000:
			os.rename(file, "LRT_0" + str(int(filename[4:9]) + OFFSET_AMOUNT) + file_extension);
		
		sleep(0.001);

def wait_input_to_exit():
    msvcrt.getch();

# ---------------------------------- #
# -------- edit directories -------- #
# ---------------------------------- #

# edit_list = [r""]

# --------------------------------------------- #
# -------- safty net - take off to run -------- #
# --------------------------------------------- #

# RUN = True

def run(edit_list):
	for item in edit_list:
		try:
			print ("Starting to run on - " + item);
			rename_method(item);
			print ("Done Running - " + item);
		except Exception as e: 
			print("An exception was thrown:");
			print(e);
			continue;
	return;

print("Starting Program\n");

if RUN == True:
	run(edit_list);
	print("Program has Finished Correctly");
else:
	print("Program did not run. RUN = False");

print("\nPlease press any key to exit");
wait_input_to_exit();
