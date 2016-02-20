import fileinput
import sys

with fileinput.FileInput("/home/pi/Cinemagraphs/frames/get_lucky.html", inplace=True, backup='.bak') as file:
	for line in file:
	#	line.replace("replace_me", "choose me")
	#	sys.stdout.write(line)
		print(line.replace("replace_me", "choose me"), end='')
fileinput.close()
