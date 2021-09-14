import os
import math
import msvcrt
import os.path
from os import listdir
from time import sleep
from os.path import isfile, join

RUN = False;
PRINT_PROGRESS = True;
g_ITER_COUNT = 0;
g_PROGRESS_COUNTER = 0;

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

	global g_ITER_COUNT, g_PROGRESS_COUNTER;

	os.chdir(PATH);

	# find allnames of the images
	guide_files = [file for file in listdir(PATH + r"\keyframes_images") if isfile(join(PATH + r"\keyframes_images", file))];

	filtered_names = [];

	for guide_file in guide_files:

		filename_guide, file_extension = os.path.splitext(guide_file);

		filtered_names.append(filename_guide);

	# find metadata files that have the same name as the images
	# metadata_files = [file for file in listdir(PATH + r"\metadata") if isfile(join(PATH + r"\metadata", file))];
	choose_files = [file for file in listdir(PATH) if isfile(join(PATH, file))];

	g_ITER_COUNT = 0;
	g_PROGRESS_COUNTER = 0;

	demuninator = math.floor(len(choose_files)/10);
	if demuninator == 0: 
		global PRINT_PROGRESS;
		PRINT_PROGRESS = False; 

	for choose_file in choose_files:

		print_process(demuninator);

		choose_filename, file_extension = os.path.splitext(choose_file);
		
		if choose_filename in filtered_names:
			os.rename(join(PATH, choose_file), join(PATH + r"\chosen", choose_filename + file_extension));
		
		sleep(0.001);

def wait_input_to_exit():
    msvcrt.getch();

# ---------------------------------- #
# -------- edit directories -------- #
# ---------------------------------- #

edit_list = [r"C:\Users\Itamar Katz\Desktop\MRO Timelaps - DNG"];

# --------------------------------------------- #
# -------- safty net - take off to run -------- #
# --------------------------------------------- #

RUN = True

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
