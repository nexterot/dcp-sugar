# -*- coding: utf-8 -*-

def remove_colons(code):
	""" 
	заменяет двоеточия на фигурные скобки 
	code - строка, содержащая sugar-код
	"""
	find_colon = code.find(':') 										# нашли индекс двоеточия
	if find_colon == -1: 												# выход из рекурсии
		return code
	else:
		code = code[:find_colon] + '{' + code[find_colon+1:] 			# поменять ':' на '{'
		current_index = code[:find_colon].find('\n') 					# нашли индекс предыдущего \n; текущий индекс
		count = 0 														# счетчик количества пробельных символов в отступе блока
		while code[current_index].isspace(): 							# до тех пор пока пробельные символы, проверять следующий символ
			count += 1
			current_index += 1											# счетчик количества пробельных символов в последующих строках,
		count_inner = 0 							 					# 		ищем конец вложенного блока
		while count_inner != count: 									# идти дальше пока не закончится вложенный блок
			count_inner = 0
			current_index = code[current_index:].find('\n')
			while code[current_index].isspace():
				count_inner += 1
				current_index += 1
		current_index -= count 												 # сдвиг назад
		code_file = code[:current_index] + '}' + '\n' + code[current_index:] # засунуть в строку '}' и '\n'
		remove_colons(code) 												 # рекурсивный вызов

if __name__ == '__main__':
	print("It's not an executive module!")
