# -*- coding: utf-8 -*-

def add_brackets(code):
    lst = [x for x in range(0,len(code)) if code[x] == '{']
    for index in lst:
        i = index
        while code[i]!= '\n':
            i-=1
        if code[i+1].isalpha():
            continue
        code = code[:index]+")"+code[index:]
        while code[index]!='\n':
            index-=1
        while not code[index].isalpha():
            index+=1;
        while not code[index].isspace():
            index+=1;
        code = code[:index]+"("+code[index+1:]
        for i in range(0, len(lst)):
            lst[i]+=1
    return code



if __name__ == "__main__":
	print("Not an executive module!")
