# -*- coding: utf-8 -*-

def remove_colon(code):
	""" 
	заменяет двоеточия на фигурные скобки 
	code - строка, содержащая sugar-код
	"""
	find_colon = code.find(':') 						# нашли индекс двоеточия
	
	if find_colon == -1: 							# выход из рекурсии
		return code
	else:
		code = code[:find_colon-1]+'{'+code[find_colon:]
		current_index = code[:find_colon].find('\n') 			# нашли индекс предыдущего \n; текущий индекс
		count = 0 							# счетчик количества пробельных символов в отступе блока
		while code[current_index].isspace(): 				# пока пробельные символы,проверять следующий символ
			count += 1
			current_index += 1
		count_inner = 0 						# счетчик количества пробельных символов
		while count_inner != count or code[current_index+1] != '\n':	# идти дальше пока не закончится вложенный блок
			print(count_inner, current_index)
			count_inner = 0
			current_index = code[current_index:].find('\n')
			while not code[current_index].isaspha() or code[current_index+1] != '\n':
				count_inner += 1
				current_index += 1
		current_index -= 1+count 					# сдвиг назад
		code_file = code[:current_index] + '}' + '\n' + code[current_index:] # засунуть в строку '}' и '\n'
		remove_colon(code) 						# рекурсивный вызов

if __name__ == '__main__':
	print("It's not an executive module!")
