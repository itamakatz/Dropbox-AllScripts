import os
from os import listdir

RUN = False

if(RUN):
	dir_where_files_to_be_deleted = r".\\Sent"
	for file in listdir(dir_where_files_to_be_deleted):
		print(file);
		# the general format is:
		# del "\\?\<full path to file>"
		os.system(fr'del "\\?\J:\Dropbox\General Stuff\Backups\GBWhatsapp Backup\Media\GBWhatsApp Audio\Sent\{file}"')
