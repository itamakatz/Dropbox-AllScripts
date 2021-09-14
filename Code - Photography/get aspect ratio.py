import os
import math
import msvcrt
import os.path
from os import listdir
from os.path import isfile, join
from PIL import Image  # uses pillow

RUN = False

file_extension_include = [".jpg", ".jpeg", ".PNG", ".gif", ".tif", ".tiff"];
file_extension_exclude = [".CR2", ".ARW"];

def include_suffix(file_extension):
	# for extension_include in map(lambda x:x.lower(), file_extension_include):
	for extension_include in file_extension_include:
		if (extension_include == file_extension):
			return True;
	return False;

def exclude_suffix(file_extension):
	for extension_exclude in map(lambda x:x.lower(), file_extension_exclude):
		if (extension_exclude == file_extension):
			return True;
	return False;

# given a path reame all the files inside
def rename_method(PATH):
	os.chdir(PATH);

	# find all files in the directory
	only_files = [file for file in listdir(PATH) if isfile(join(PATH,file))];

	for file in only_files:

		# get the name and suffix of the file
		_ , file_extension = os.path.splitext(file);

		# exclude RAW images and notice user about it
		if (exclude_suffix(file_extension.lower())):
			print(file + " - is a RAW image. PIL can not open it\n");
			continue;

		# exclude all files except with suffix from file_extension_include 
		if (not include_suffix(file_extension.lower())): continue;

		im = Image.open(PATH + "\\" + file);
		(width, height) = im.size;
		gcd = math.gcd(width, height);

		print(file);

		print("\t(W, H) - (" + str(width) + "," + str(height) + ")");  # return value is a tuple, ex.: (1200, 800)

		print("\tAspect Retio - " + str(int(width/gcd)) + ":" + str(int(height/gcd)));
		print("\tPortrait");

		print("\n");

def wait_input_to_exit():
    msvcrt.getch()

# ---------------------------------- #
# -------- edit directories -------- #
# ---------------------------------- #

edit_list = [r"F:\Dropbox\Media\Fotos\Edited\Lightroom Exports\Italy"]

# edit_list = [r""]
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


