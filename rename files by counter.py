import os
import math
import msvcrt
import os.path
from os import listdir
from time import sleep
from os.path import isfile, join

RUN = False;
PRINT_PROGRESS = True;
RENAME_FROM_NUM = 1;

# given a path reame all the files inside
def rename_method(PATH):
	os.chdir(PATH);

	# find all files in the directory
	only_files = [file for file in listdir(PATH) if isfile(join(PATH,file))];

	iter_counter = 0;
	progress_counter = 0;
	demuninator = math.floor(len(only_files)/10);
	if demuninator == 0: 
		global PRINT_PROGRESS;
		PRINT_PROGRESS = False; 
		
	rename_counter = 1;

	for file in only_files:

		if PRINT_PROGRESS == True and math.floor(iter_counter / demuninator) == progress_counter + 1:
			progress_counter += 1;
			print("\tDone " + str(progress_counter * 10) + "%")			

		iter_counter += 1;

		filename, file_extension = os.path.splitext(file);
		os.rename(file, str(rename_counter) + file_extension);

		rename_counter += 1;
		
		sleep(0.001);

def wait_input_to_exit():
    msvcrt.getch();

# ---------------------------------- #
# -------- edit directories -------- #
# ---------------------------------- #

# edit_list = [r""]
# edit_list = [r"C:\Users\Itamar\Desktop\100EOS5D"]
# edit_list = [r"C:\Users\Itamar\Desktop\100MSDCF"]

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
