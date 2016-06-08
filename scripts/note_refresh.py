import urllib.request
import fileinput
from os import system

localNotePath = "/home/pi/Cinemagraphs/notes/Notes.txt"
remoteNotePath = "https://www.dropbox.com/s/nh8o4gou047td5m/Notes.txt?dl=1"

# Download the notes from remoteNotePath and save it locally under localNotePath:
with urllib.request.urlopen(remoteNotePath) as response, open(localNotePath, 'wb') as out_file:
    data = response.read() # a `bytes` object
    out_file.write(data)


# fixing line end chars
with fileinput.FileInput(localNotePath, inplace=True, backup='.bak') as file:
	for line in file:
		print(line, end='')
fileinput.close()

# backs up and updates html files
system("python3 update_html.py")
