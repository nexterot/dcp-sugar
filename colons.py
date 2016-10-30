# -*- coding: utf-8 -*-

def remove_colons(code):
    index = code.find(':')
    if index == -1:
        return code
    code = code[:index]+" {"+code[index+1:]
    index = code.find('\n', index)
    count = 0
    while code[index+1].isspace():
        count+=1
        index+=1
    count_inner = count
    while index < (len(code)-1) and count <= count_inner:
        count_inner = 0
        index = code.find('\n', index)
        while index < (len(code)-1) and code[index+1].isspace():
            count_inner+=1
            index+=1
    code = code[:index]+"\n"+(count-1)*'\t'+"}"+'\n'+code[index:]
    return remove_colons(code)
    
    

if __name__ == '__main__':
    print("It's not an executive module!")
