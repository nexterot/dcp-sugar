# -*- coding: utf-8 -*-

def replace_or_and(code):
	and_idx = code.find(" and ")
	or_idx = code.find(" or ")
	
	while and_idx != -1:
		code = code[:and_idx] + " &&" + code[and_idx+4:]
		and_idx = code.find(" and ")
		
	while or_idx != -1:
		code = code[:or_idx] + " || " + code[or_idx+4:]
		or_idx = code.find(" or ")
			
	return code
	
	
if __name__ == "__main__":
	print("Not an executive module!")
	
