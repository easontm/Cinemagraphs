#!/usr/bin/python3

import glob, os
import fileinput
from subprocess import call

localNotePath = '/home/pi/Cinemagraphs/notes/Notes.txt'
framesDir = '/home/pi/Cinemagraphs/frames'


fileList = []
with open(localNotePath, 'r') as noteFile:
 	noteText=noteFile.read()


os.chdir(framesDir)
for file in glob.glob("*.html"):
	fileList.append(file)

templateList = []
for file in glob.glob("*.tmplt"):
	templateList.append(file)

# copy contents of templates to reset html to base state
itr = iter(templateList)
for fileName in fileList:
	call(["cp", next(itr), fileName])
fileinput.close()

# base state contains replace_me phrase. note contents loaded here
with fileinput.FileInput(fileList, inplace=True, backup='.bak') as file:
	for line in file:
		print(line.replace("replace_me", noteText), end='')		
fileinput.close()
