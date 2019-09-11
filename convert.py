import os
import sys
from tinytag import TinyTag

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
#root.withdraw()

file_path = filedialog.askdirectory()
print("file path: " + file_path)

def get_file_list(directory):
	os.chdir(directory)
	file_list = os.listdir()
	return file_list

def generate_playlist(file_list):
	path = os.getcwd()
	output = ""
	for song in file_list:
		if ".mp3" in song:
			tag = TinyTag.get(song)
			filesize = tag.filesize
			artist = tag.artist
			title = tag.title
			length = tag.duration
			tags = [filesize, artist, title, length]
			song_str = "EXTVJD:<filesize>{}</filesize><artist>{}</artist><title>{}</title><songlength>{}</songlength>".format(*tags)
			song_str += "\n" + path + "\\" + song + "\n"
			output += song_str
	return output
	
def main():
	directory = file_path
	file_list = get_file_list(directory)
	text = generate_playlist(file_list)
	f = filedialog.asksaveasfile(mode='w', defaultextension='.m3u')
	if f is None:
		return
	f.write(text)
	f.close()

if __name__ == "__main__":
	main()