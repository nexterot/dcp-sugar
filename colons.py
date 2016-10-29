# -*- coding: utf-8 -*-
#hahaha
def remove_colons(code):
    index = code.find(':')
    if index == -1:
        return code
    code = code[:index]+"{"+code[index+1:]
    index += code[index:].find('\n')
    count = 0
    while code[index+1].isspace():
        count+=1
        index+=1
    count_inner = count
    while index < (len(code)-1) and count_inner >= count:
        count_inner = 0
        index+=code[index:].find('\n')
        while index < (len(code)-1) and code[index+1].isspace():
            count_inner+=1
            index+=1
    code = code[:index]+"}"+"\n"+code[index:]
    return remove_colons(code)
    
        
if __name__ == '__main__':
    print("It's not an executive module!")
i = 5
