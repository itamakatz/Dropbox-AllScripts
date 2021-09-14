import re
import sys

# Set the path of the "timedtext" file and if the CC was automatically generated

isAutoCc = True
# isAutoCc = False
FILE_PATH = r"C:\Users\itama\Desktop\CC_from_youtube"

# safety check not to anciently do something
# run = True
run = False

if(isAutoCc):
	regs = [(r"(^((?![\.]$).)*$)\n", ""),
			(r'\s*"utf8": "(.*)"', r"\1"),
			(r"(^((?![\.]$).)*$)\n", r"\1"),
			(r"\\n"," "),
			(r",   ", r"\n"),
			(r",\s+", r" ")
			]
else:
	regs = [(r"(^((?![\.]$).)*$)\n", ""),
		(r'\s*"utf8": "(.*)"', r"\1"),
		(r"(^((?![\.]$).)*$)\n", r"\1"),
		(r"\\n"," "),
		]

if(not run): sys.exit()

with open(FILE_PATH + ".txt") as f:
    all_lines = f.read()

for reg in regs:
	all_lines = re.sub(reg[0],reg[1], all_lines)

all_lines = all_lines[:-1]

text_file = open(FILE_PATH + r"_new.txt", "w")
text_file.write(all_lines)
text_file.close()