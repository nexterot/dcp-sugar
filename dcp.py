#!/usr/bin/env
# -*- coding: utf-8 -*-

import sys

# функция, меняющая ':' на '{ }'
from colons import remove_colons

def main():
	### Чтение файла
	if (len(sys.argv) != 2):
		print("Usage: python dcp <program.sugar>")
		exit(1)
	file_name = sys.argv[1]
	if len(file_name) <= 6:
		print("Invalid file name: " + file_name)
		exit(1)
	file_extension = file_name[-6:]
	if (file_extension != ".sugar"):
		print("Usage: python dcp <program.sugar>")
		exit(1)
	out_file_name = file_name[:-6] + '.c'
	try:
		source = open(file_name, 'r')
	except IOError:
		print("Error reading/writing to files: "+file_name+', '+out_file_name)
		exit(1)
	else:
		sugar_code = source.read()
		### Разбор выражений
		# итоговый файл
		c_code = sugar_code
		c_code = remove_colons(c_code)
		### Запись си-файла
		out_file = open(out_file_name, 'w')
		out_file.write(c_code)
		out_file.close()
	
if __name__ == '__main__':
	main()
