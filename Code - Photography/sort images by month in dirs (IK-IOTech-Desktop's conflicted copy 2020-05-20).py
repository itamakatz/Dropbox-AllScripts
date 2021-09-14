import os
import math
import msvcrt
import shutil
from os import listdir
from os.path import isfile, join
import os.path, time

RUN = False
DATE_INDEX = 8;
PRINT_PROGRESS = True;

# define list of all the month's
months_list = [("Jan", "01"), ("Feb", "02"), ("Mar", "03"), \
				("Apr", "04"), ("May", "05"), ("Jun", "06"),\
				("Jul", "07"), ("Aug", "08"), ("Sep", "09"),\
				("Oct", "10"), ("Nov", "11"), ("Dec", "12")];

file_extension_exclude = [".xmp", ".ini", ".dropbox"];

def exclude_suffix(file_extension):
	for extension_exclude in  map(lambda x:x.lower(), file_extension_exclude):
		if (extension_exclude == file_extension):
			return True;
	return False;

# given a path reame all the files inside
def rename_method(PATH):
	os.chdir(PATH);

	# find all files in the directory
	only_files = [join(PATH, file) for file in listdir(PATH) if isfile(join(PATH, file))];
	only_files.sort(key=lambda x: os.path.getsize(x));

	iter_counter = 0;
	progress_counter = 0;
	demuninator = math.floor(len(only_files)/10);
	if demuninator == 0: 
		global PRINT_PROGRESS;
		PRINT_PROGRESS = False; 
		
	for file in only_files:

		if PRINT_PROGRESS and math.floor(iter_counter / demuninator) == progress_counter + 1:
			progress_counter += 1;
			print("\tDone " + str(progress_counter * 10) + "%")			

		iter_counter += 1;

		# opening the file to get the relevant data out of it. then closing it
		opend_file = os.open(file, os.O_RDONLY);
		time_string = time.ctime(os.stat(opend_file)[DATE_INDEX]);
		os.close(opend_file);
		
		# change the month from a name to a number 
		for month in months_list:
			time_string = time_string.replace(str(month[0]), str(month[1]));

		# parsing the date in time_string
		month = time_string[4:6];

		# if there is no dir, create it
		if not os.path.exists("./" + month):
			os.makedirs("./" + month);

		# get the name and suffix of the file
		filename, file_extension = os.path.splitext(file);

		# exclude files with suffix from file_extension_exclude 
		if (exclude_suffix(file_extension.lower())): continue;
		
		shutil.move("./" + filename + file_extension, "./" + month + "/" + filename + file_extension);

def wait_input_to_exit():
    msvcrt.getch()

# ---------------------------------- #
# -------- edit directories -------- #
# ---------------------------------- #

# edit_list = [r"C:\Users\Itamar\Desktop\100EOS5D"]
# edit_list = [r"C:\Users\Itamar\Desktop\100MSDCF"]
edit_list = [r"C:\Users\Itamar Katz\Desktop\OnePlus 6\DCIM\LightroomCamera"]

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
