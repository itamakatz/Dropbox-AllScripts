#  -*- coding: utf-8 -*-
import os
import msvcrt
from os import listdir
from os.path import isfile, join
from mutagen.easyid3 import EasyID3

RUN = False
DATE_INDEX = 8;

# given a path rename all the files inside
def rename_method(PATH):
	os.chdir(PATH);

	# find all files in the directory
	only_files = [file for file in listdir(PATH) if isfile(join(PATH,file))];

	g_index = 0;

	for file in only_files:

		try:
			str_path = PATH + "\\" + file;
			print(str_path);
			audio = EasyID3(str_path)
			audio['title'] = u""
			audio['artist'] = u""
			audio['album'] = u""
			audio['composer'] = u"" # clear
			audio.save()
			print ("Done Running - " + file);
			os.rename(file, str(g_index) + ".mp3");
			g_index = g_index + 1;

		except Exception as e: 
			# print ("problem at index - " + g_index);
			print ("problem at index");
			print (e);
			break;



def wait_input_to_exit():
	msvcrt.getch()

# ---------------------------------- #
# -------- edit directories -------- #
# ---------------------------------- #

edit_list = [r"C:\Users\Itamar\Desktop\all\a14"]
# edit_list = [r"H:\DCIM\102MSDCF"]
# edit_list = [r"G:\DCIM\100EOS5D"]
# edit_list = [r"H:\DCIM\100EOS5D"]
# edit_list = [r"H:\PRIVATE\AVCHD\BDMV\STREAM"]
# edit_list = [r"C:\Users\Itamar\Desktop\102MSDCF"]
# edit_list = [r"E:\Dropbox\Media\Fotos\Photography Fotos"]

# works with all files exept .xmp
def run(edit_list):
	for item in edit_list:
		try:
			rename_method(item);
			print ("Done Running - " + item);
		except Exception as e: 
			print(e);
			print ("No such directory - " + item);
			continue;
	return;


# --------------------------------------------- #
# -------- safty net - take off to run -------- #
# --------------------------------------------- #

# RUN = True

print(u"Starting Program\n");

if RUN == True:
	run(edit_list);
	print("Program has Finished Correctly");
else:
	print("Program did not run. RUN = False");


print("\nPlease press any key to exit");
wait_input_to_exit();
