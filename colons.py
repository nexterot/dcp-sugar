# -*- coding: utf-8 -*-

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
<<<<<<< HEAD
        all_spaces = True
        for c in range(index+1, code.find('\n', index+1)):
            if not code[c].isspace() and all_spaces:
                all_spaces = False
        if all_spaces:
            index = code.find('\n', index+1)
        while index < (len(code)-1) and code[index+1].isspace():
            count_inner+=1
            index+=1
    code = code[:index]+"\n"+"}"+"\n"+code[index:]
    return remove_colons(code)

=======
        while index < (len(code)-1) and code[index+1].isspace():
            count_inner+=1
            index+=1
    code = code[:index]+"}"+"\n"+code[index:]
    return remove_colons(code)
    
        
>>>>>>> bc7c690f7c0b5b2611bfead3fbe87bff053c03a9
if __name__ == '__main__':
    print("It's not an executive module!")
