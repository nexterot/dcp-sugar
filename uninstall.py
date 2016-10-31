#!/usr/bin/env python3

import sys

def remove_string():
	
	if len(sys.argv) != 3:
		print("Usage <file> <string>")
		exit(1)
	
	file = open(sys.argv[1], 'r+')
	string = sys.argv[2]
	content = file.read()
	index = content.find(string)
	
	if index != -1:
		content = content[:index] + content[index+len(string):]
		file.write(content)
	file.close()	
	
	
if __name__ == "__main__":
	remove_string()
