import os
import math
import msvcrt
from os import listdir
from os.path import isfile, join
import os.path, time

#########################
##### Magic Numbers #####
#########################

PRINT_PROGRESS = True;
file_extension_exclude = [".xmp", ".ini", ".dropbox"];

#########################
####### Constants #######
#########################

RUN = False
DATE_INDEX = 8;
# define list of all the month's
months_list = [("Jan", "01"), ("Feb", "02"), ("Mar", "03"),\
							("Apr", "04"), ("May", "05"), ("Jun", "06"),\
							("Jul", "07"), ("Aug", "08"), ("Sep", "09"),\
							("Oct", "10"), ("Nov", "11"), ("Dec", "12")];

#########################
#########################

def check_exclude_files(file_extensions):
	'''
	Check is there is at least one extension which should not be excluded.
	'''
	for extension in file_extensions:
		if(not check_extension(extension)):
			return False
	return True

def check_extension(file_extension):
	'''
	Exclude the files defined in the file_extension_exclude list
	'''
	for extension_exclude in map(lambda x:x.lower(), file_extension_exclude):
		if (extension_exclude == file_extension.lower()):
			return True;
	return False;

def check_already_renamed(file_name, year, month, day, hour, minute, second):
	return year + "-" + month + "-" + day + " " + hour + "." + minute + "." + second in file_name

def get_dropbox_format(year, month, day, hour, minute, second, count, extension):
	if(count == 0):
		return year + "-" + month + "-" + day + " " + hour + "." + minute + "." + second + extension
	else:
		return year + "-" + month + "-" + day + " " + hour + "." + minute + "." + second + "-" + str(count) + extension

def rename_recursive(path):
	'''
	Recursively rename all files withing the current path and all sub files
	'''
	for subDir in [ os.path.join(path, name) for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ]:
		rename_recursive(subDir);
	print ("Renaming files in: " + "'" + path + "'");
	rename_files(path);
	print ("Finished Renaming files in: " + "'" + path + "'");

def rename_files(path):
	'''
	given a dir, rename all the non-nested files inside it.
	in case of metadata, give the metadata the same name as the file.
	'''
	os.chdir(path);

	# find all files in the directory
	only_files = [join(path, file) for file in listdir(path) if isfile(join(path, file))];
	# first sore by size and then by name -> the first extension in the list of extensions will represent the largest file
	only_files.sort(key=lambda x: os.path.getsize(x)); 
	only_files.sort(key=str.lower);
	
	files_tuple = [os.path.splitext(file) for file in only_files]

	files_with_meta_dict = {}
	
	for file_tuple in files_tuple:
		if file_tuple[0] not in files_with_meta_dict:
			files_with_meta_dict[file_tuple[0]] = [file_tuple[1]]
		else:
			files_with_meta_dict[file_tuple[0]].append(file_tuple[1])

	#if there are not files just return
	if(not files_with_meta_dict): return

	##########################
	##### Print progress #####
	##########################

	iter_counter = 0;
	progress_counter = 0;
	denominator = math.floor(len(files_with_meta_dict.keys())/10);
	if denominator == 0: 
		global PRINT_PROGRESS;
		PRINT_PROGRESS = False; 

	##########################

	for file_name in files_with_meta_dict.keys():

		if PRINT_PROGRESS and math.floor(iter_counter / denominator) == progress_counter + 1:
			progress_counter += 1;
			print("\tDone " + str(progress_counter * 10) + "%")

		iter_counter += 1;

		# opening the file to get the relevant data out of it. then closing it
		opened_file = os.open(file_name + files_with_meta_dict[file_name][0], os.O_RDONLY);
		time_string = time.ctime(os.stat(opened_file)[DATE_INDEX]);
		os.close(opened_file);
		
		#################################################################################################################################################
		######################################################### Extract the date of the file ##########################################################
		#################################################################################################################################################

		# change the month from a name to a number 
		for month in months_list:
			time_string = time_string.replace(str(month[0]), str(month[1]));

		# parsing the date in time_string
		month = time_string[4:6];
		day = time_string[7:9];
		year =time_string[19:];
		hour = time_string[10:12];
		minute = time_string[13:15];
		second = time_string[16:18];

		day = day.replace(" ", "0");

		# change back the month from number to name 
		# for month_pair in months_list:
		# 	month = month.replace(str(month_pair[1]), str(month_pair[0]));

		# excludes if all the extensions are from the file_extension_exclude list
		if (check_exclude_files(files_with_meta_dict[file_name])): continue;

		#################################################################################################################################################
		############################################################### Create nested dir ###############################################################
		#################################################################################################################################################
		
		current_dir_relative = os.path.split(os.path.abspath(path))[1]
		
		# if our path is already the correct dir then new_dir = path
		if current_dir_relative == year + " - " + month:
			new_dir = path
			# NOTE: if the file has already been renamed, exclude it
			if (check_already_renamed(file_name, year, month, day, hour, minute, second)): continue;
		else:
			new_dir = os.path.join(path, year + " - " + month);
			if not os.path.exists(new_dir):
				os.makedirs(new_dir)

		#################################################################################################################################################
		#################################################### Rename the file while avoiding conflicts  ##################################################
		#################################################################################################################################################

		count = 0; # count number of times a file has multiple names 
		
		# This while is just in case we have multiple files with same name
		while (True):
			valid_name = True
			for extension in files_with_meta_dict[file_name]:
				d_format = get_dropbox_format(year, month, day, hour, minute, second, count, extension)
				to_rename_file = os.path.join(new_dir, d_format)
				if(os.path.isfile(to_rename_file)):
					valid_name = False
			
			if(not valid_name):
				count += 1;
			else:
				break
		
		for extension in files_with_meta_dict[file_name]:
			current_file = file_name + extension
			os.rename(current_file, os.path.join(new_dir, get_dropbox_format(year, month, day, hour, minute, second, count, extension)))

		#################################################################################################################################################
		#################################################################################################################################################

def wait_input_to_exit():
	msvcrt.getch()

# ---------------------------------- #
# -------- edit directories -------- #
# ---------------------------------- #

rename_list = [r"H:\Test"]

# ---------------------------------------------- #
# -------- safety net - take off to run -------- #
# ---------------------------------------------- #

# RUN = True

def run(rename_list):
	for item in rename_list:
		try:
			if(not os.path.isdir(item)): 
				print ("Path: " + "'" + item + "'" + " is not a dir, therefore skipping..");
				continue;
			print ("Starting to run on - " + item);
			rename_recursive(item);
			print ("Done Running - " + item);
		except Exception as e: 
			print("An exception was thrown:");
			print(e);
			continue;
	return;

print("Starting Program\n");

if RUN == True:
	run(rename_list);
	print("Program has Finished Correctly");
else:
	print("Program did not run. RUN = False");

print("\nPlease press any key to exit");
wait_input_to_exit();
