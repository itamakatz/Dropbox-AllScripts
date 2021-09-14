import os
import math
import errno
import msvcrt
import os.path
import itertools
from os import listdir
from os.path import isfile, join
import os.path, time

RUN = False
DATE_INDEX = 8;

# define list of all the month's
months_list = [("Jan", "01"), ("Feb", "02"), ("Mar", "03"), \
				("Apr", "04"), ("May", "05"), ("Jun", "06"),\
				("Jul", "07"), ("Aug", "08"), ("Sep", "09"),\
				("Oct", "10"), ("Nov", "11"), ("Dec", "12")];

file_extension_include = [".jpg", ".jpeg", ".PNG", ".gif", ".tif", ".tiff", ".CR2", ".ARW"];

def include_suffix(file_extension):
	# for extension_include in map(lambda x:x.lower(), file_extension_include):
	for extension_include in file_extension_include:
		if (extension_include == file_extension):
			return True;
	return False;

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
	only_files = [file for file in listdir(PATH) if isfile(join(PATH,file))];

	for file in only_files:

		opend_file = os.open(file, os.O_RDONLY);
		time_string = time.ctime(os.stat(opend_file)[DATE_INDEX]);
		os.close(opend_file);
		
		# change the month from a name to a number 
		for month in months_list:
			time_string = time_string.replace(str(month[0]), str(month[1]));

		# parsing the date in time_string
		month = time_string[4:6];

		# get the name and suffix of the file
		_ , file_extension = os.path.splitext(file);
		print("BEFORE\n");

		# exclude all files except with suffix from file_extension_include 
		if (not include_suffix(file_extension.lower())): continue;
		print("AFTER\n");

		check_dir_exists(PATH + "\\" + month);
		os.rename(PATH + "\\" + file, PATH + "\\" + month + "\\" + file);

		print("\n");

def wait_input_to_exit():
    msvcrt.getch()

# ---------------------------------- #
# -------- edit directories -------- #
# ---------------------------------- #

# edit_list = [r"C:\Users\Itamar Katz\Desktop\New folder"]

edit_list = [r"C:\Users\Itamar Katz\Desktop\TEST"]
# edit_list = [r"H:\DCIM\102MSDCF"]

# --------------------------------------------- #
# -------- safty net - take off to run -------- #
# --------------------------------------------- #

# RUN = True

# works with all files exept .xmp
def run(edit_list):
	for item in edit_list:
		try:
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


