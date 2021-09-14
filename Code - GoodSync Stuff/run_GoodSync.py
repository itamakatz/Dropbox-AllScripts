import os
import msvcrt

def wait_input_to_exit():
	msvcrt.getch()

print("starting program");

PATH_DIR = r"F:\Dropbox\General Stuff\CodeGoodSync_before_delete.py";

os.system('python F:\Dropbox\General/ Stuff\CodeGoodSync_before_delete.py &');

print("\nPlease press any key to exit");
wait_input_to_exit();