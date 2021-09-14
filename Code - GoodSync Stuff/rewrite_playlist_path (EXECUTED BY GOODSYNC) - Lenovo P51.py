import os
import re
import os.path
from os import listdir
from os.path import isfile, join

RUN = False

PATH = r"C:\Users\Itamar\Dropbox\Media\Music\Playlists";

# given a path reame all the files inside
def rename_method():

	os.chdir(PATH);

	# find all files in the directory
	only_files = [file for file in listdir(PATH) if isfile(join(PATH,file))];

	for file in only_files:
	
		filename, file_extension = os.path.splitext(file);
		
		print('Working on file: ' + filename);

		# if its not a playlist file - m3u - skip it
		if (file_extension.lower() != ".m3u"): continue;

		# os.rename(PATH + "\\" + file, PATH + r"\temp");

		# with open(PATH + r"\temp") as o_file:
			
		# 	o_file.close();

		with open(PATH + "\\" + file, 'r+', encoding="utf8") as o_file:
			lines = o_file.readlines();
			o_file.seek(0);
			for line in lines:
				line = re.sub(r'\\', '/', line);
				line = re.sub('(.*)(Music - Selected Songs)', r'../Music - Selected Songs', line);
				o_file.write(line);

			o_file.truncate();
			o_file.close();

		# os.remove(PATH + r"\temp");

	print();

# RUN = True

print("Starting Program\n");

if RUN == True:
	try:
		rename_method();
		print ("Done Running");
	except Exception as e: 
		print("An exception was thrown:");
		print(e);

	print("Program finished");
else:
	print("Program did not run. RUN = False");


# Use one of the two approaches. Either sleep for a given time or wait for user key.

# Wait for given sec
import time
time.sleep(1);

# # wait for user key press
# import msvcrt

# def wait_input_to_exit():
#     msvcrt.getch()

# print("\nPlease press any key to exit");
# wait_input_to_exit();