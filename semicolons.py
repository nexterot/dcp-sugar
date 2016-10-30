# -*- coding: utf-8 -*-

def add_semicolons(code):
	i = 0
	x = len(code)-1
	lst = ["#", "}", "{"]
	while i <= x:
		if code[i] in lst:
			i = skip(i, code)
			continue
		if code[i] == '\n' and code[i-1]!='\n':
			code = code[:i]+";"+code[i:]
			i+=1
		i+=1
		x = len(code)-1
	return code


def skip(n, code):
	while n <= (len(code)-1) and code[n]!='\n':
		n+=1
	return n+1
if __name__ == "__main__":
	print("Not an executive module!")
