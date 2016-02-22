import urllib.request
import fileinput
from os import system

# Download the file from `url` and save it locally under `file_name`:
with urllib.request.urlopen('https://www.dropbox.com/s/nh8o4gou047td5m/Notes.txt?dl=1') as response, open('/home/pi/Cinemagraphs/Notes.txt', 'wb') as out_file:
    data = response.read() # a `bytes` object
    out_file.write(data)


with fileinput.FileInput("/home/pi/Cinemagraphs/Notes.txt", inplace=True, backup='.bak') as file:
	for line in file:
		print(line, end='')
fileinput.close()

system("python3 update_html.py")
