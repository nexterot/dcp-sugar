#!/usr/bin/env
# -*- coding: utf-8 -*-

import sys
#import string

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
		c_code = remove_colon(sugar_code)
		### Запись си-файла
		out_file = open(out_file_name, 'w')
		out_file.write(c_code)
		out_file.close()
		
def remove_colon(code):
	""" 
	заменяет двоеточия на фигурные скобки 
	code - строка, содержащая sugar-код
	"""
	find_colon = code.find(':') # нашли индекс двоеточия
	if find_colon == -1: # выход из рекурсии
		return code
	else:
		current_index = code[:find_colon].find('\n') # нашли индекс предыдущего \n; текущий индекс
		count = 0 # счетчик количества пробельных символов в отступе блока
		while code[current_index].isspace(): # до тех пор пока пробельные символы, проверять следующий символ
			count += 1
			current_index += 1
		count_inner = 0 # счетчик количества пробельных символов в последующих строках, ищем конец вложенного блока
		while count_inner != count: # идти дальше пока не закончится вложенный блок
			print(count_inner, current_index)
			count_inner = 0
			current_index = code[current_index+1:].find('\n')
			while code[current_index].isspace():
				count_inner += 1
				current_index += 1
		current_index -= 1+count # сдвиг назад
		code_file = code[:current_index] + '}' + '\n' + code[current_index:] # засунуть в строку '}' и '\n'
		remove_colon(code) # рекурсивный вызов
	
if __name__ == '__main__':
	main()
