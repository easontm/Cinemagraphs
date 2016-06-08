#!/usr/bin/python3

import glob, os
import fileinput
from subprocess import call

fileList = []
with open('/home/pi/Cinemagraphs/Notes.txt', 'r') as noteFile:
	noteText=noteFile.read()


os.chdir("/home/pi/Cinemagraphs/frames")
for file in glob.glob("*.html"):
	fileList.append(file)

templateList = []
for file in glob.glob("*.tmplt"):
	templateList.append(file)

itr = iter(templateList)
for fileName in fileList:
	call(["cp", next(itr), fileName])
fileinput.close()


with fileinput.FileInput(fileList, inplace=True, backup='.bak') as file:
	for line in file:
		print(line.replace("replace_me", noteText), end='')		
fileinput.close()
