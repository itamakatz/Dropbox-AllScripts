import os
import math
import errno
import msvcrt
import os.path
import itertools
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

def get_closest_gcd(width, height):
	all_width = [width-1, width, width+1];
	all_hight = [height-1, height, height+1];
	
	all_permutations = list(itertools.product(all_width, all_hight));
	all_gcd = list(map(lambda pair: math.gcd(pair[0], pair[1]), all_permutations));
	max_gcd = max(all_gcd);

	for c_width, c_height in all_permutations:
		if math.gcd(c_width, c_height) == max_gcd:
			return (c_width, c_height, max_gcd);
	
	return (width, height, max_gcd)

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
		im.close();
		(width, height, gcd) = get_closest_gcd(width, height);
		

		print(file)

		print("\t(W, H) - (" + str(width) + "," + str(height) + ")");

		check_dir_exists(PATH + "\\" + str(int(width/gcd)) + "X" + str(int(height/gcd)));
		os.rename(PATH + "\\" + file, PATH + "\\" + str(int(width/gcd)) + "X" + str(int(height/gcd)) + "\\" + file);

		print("\n");

def wait_input_to_exit():
    msvcrt.getch()

# ---------------------------------- #
# -------- edit directories -------- #
# ---------------------------------- #

edit_list = [r"C:\Users\Itamar Katz\Desktop\New folder"]

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


