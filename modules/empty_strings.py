# -*- coding: utf-8 -*-

def remove_empty_strings(code):
    list_of_strings = code.split('\n')
    new_list = []
    for string in list_of_strings:
        if not string.isspace() and string:
            new_list.append(string)
    code = '\n'.join(new_list) + '\n'*2
    return code

	
	
if __name__ == "__main__":
	print("Not an executive module!")
