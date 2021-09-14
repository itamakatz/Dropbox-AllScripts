import os
import shutil
import sys, traceback
import time
import msvcrt
import subprocess
from time import gmtime, strftime

RUN = False;

PROCESS_NAME = r"GoodSync-v10.exe";
RUN_EXE = r"C:\Program Files\Siber Systems\GoodSync\GoodSync-v10.exe"
# PATH_DIR = r"C:\Users\Itamar\Desktop\AA\BB";
PATH_DIR = r"E:\Photography Media\Photography Fotos\RAW\_gsdata_";
WAIT_TIME_BEFORE_s = 7.5 * 60 * 60;
WAIT_TIME_AFTER_s = 5 * 60;

def wait_input_to_exit():
	msvcrt.getch()

print("Starting Program\n");

# print("\nPlease press any key to continue");
# wait_input_to_exit();

def kill_process (process_name):
	try:
		subprocess.call('taskkill /f /im ' + process_name);
	except Exception as e: 
		print(e)

def delete_dir (path_dir):
	try:
		shutil.rmtree(path_dir);
	except Exception as e: 
		print(e)

def run_process (process_name):
	try:
		subprocess.call(process_name);
	except Exception as e: 
		print(e)

RUN = True;

print("Time of execution: " + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + "\n");

# import pause
# from datetime import datetime
# pause.until(datetime(strftime("%Y", gmtime()), strftime("%m", gmtime()), strftime("%d", gmtime()), 8));

if RUN == True:
	try:
		print("waiting for: " + str(WAIT_TIME_BEFORE_s) + " seconds BEFORE killing");
		print("waiting for: " + str(WAIT_TIME_BEFORE_s / 60) + " minutes BEFORE killing");
		print("waiting for: " + str(WAIT_TIME_BEFORE_s / 60 / 60) + " hours BEFORE killing");
		
		time.sleep(WAIT_TIME_BEFORE_s);

		print("Sleeping time finished");

		print("Killing process: " + PROCESS_NAME);

		kill_process(PROCESS_NAME);
		
		print("Process killed..\n");
		print("waiting for: " + str(WAIT_TIME_AFTER_s) + " seconds AFTER killing");
		
		time.sleep(WAIT_TIME_AFTER_s);

		print("Sleeping time finished");
		# print("\nDeleting dir: " + PATH_DIR);

		# delete_dir(PATH_DIR);
		
		# print("Dir deleted\n");
		print("Running program: " + RUN_EXE);

		run_process(RUN_EXE);

		print("Program run\n");
		print("Scripts has Finished Correctly");
	
	except Exception as e: 
		print (e);
else:
	print("Program did not run. RUN = False");

# print("\nPlease press any key to exit");
# wait_input_to_exit();