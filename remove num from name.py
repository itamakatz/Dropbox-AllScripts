import os
import os.path
from os import listdir
from os.path import isfile, join

RUN = False

# given a path reame all the files inside
def rename_method():

	os.chdir(PATH);

	# find all files in the directory
	only_files = [file for file in listdir(PATH) if isfile(join(PATH,file))];

	for file in only_files:
	
		filename, file_extension = os.path.splitext(file);

		new_filename_list = []
		found_first_alpha = False

		for ch in filename:
			if(found_first_alpha):
				new_filename_list.append(ch);
				continue;
			elif ch.isalpha():
				found_first_alpha = True;
				new_filename_list.append(ch);
		
		new_filename = ''.join(new_filename_list);

		os.rename(PATH + "\\" + file, PATH + "\\" + new_filename + file_extension);


PATH = r"";

# RUN = True

print("Starting Program\n");

if RUN == True:
	try:
		rename_method();
		print ("Done Running");
	except Exception as e: 
		print(e);

	print("Program finished");
else:
	print("Program did not run. RUN = False");

# import msvcrt

# def wait_input_to_exit():
#     msvcrt.getch()

# print("\nPlease press any key to exit");
# wait_input_to_exit();