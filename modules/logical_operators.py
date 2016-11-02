# -*- coding: utf-8 -*-

def replace_or_and(code):
	and_idx = code.find(" and ")
	or_idx = code.find(" or ")
	
	while and_idx != -1:
		code = code[:and_idx] + " && " + code[and_idx+5:]
		and_idx = code.find(" and ")
		
	while or_idx != -1:
		code = code[:or_idx-1] + " || " + code[or_idx+3:]
		or_idx = code.find(" or ")
			
	return code
	
	
if __name__ == "__main__":
	print("Not an executive module!")
	
