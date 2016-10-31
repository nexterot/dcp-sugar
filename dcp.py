#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# функция, удаляющая пустые строки
from modules.empty_strings import remove_empty_strings
# функция, меняющая ':' на '{ }'
from modules.colons import remove_colons
# функция, добавляющая '()' в for, while, и т.д.
from modules.brackets import add_brackets
# функция, удаляющая ';'
from modules.semicolons import add_semicolons


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
		# убрать все пустые строки
		c_code = remove_empty_strings(c_code)
		# заменить двоеточия
		c_code = remove_colons(c_code)
		# снова убрать все пустые строки
		c_code = remove_empty_strings(c_code)
		# добавить '()' в циклы и т.п.
		c_code = add_brackets(c_code)
		# добавить ';'
		c_code = add_semicolons(c_code)
		### Запись си-файла
		out_file = open(out_file_name, 'w')
		out_file.write(c_code)
		out_file.close()


if __name__ == '__main__':
	main()
