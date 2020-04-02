#TO CHECK A VALID IDENTIFIER NAME IN PYTHON

import keyword

identifier_name=input('Enter your identifier to check valid or not: ')

LOWER_CASE_ALPHABETS=['a','b','c','d','e','f','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
UPPER_CASE_ALPHABETS=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
INVALID_SPECIAL_CHARACTERS=[' ','+','-','*','/','%','~','`','!','@','#','$','^','&','(',')','=','\\','|','{','}','[',']',';',':',',','.','<','>','/','?','\'','\"']
KEYWORD_LIST=keyword.kwlist

'''new things used:
1.Usage of backslash
2.Using \ to treat special symbols as a normal characters-- see INVALID_SPECIAL_CHARACTERS'''

if identifier_name[0]!='_' and identifier_name[0] not in LOWER_CASE_ALPHABETS and \
   identifier_name[0] not in UPPER_CASE_ALPHABETS:
	pass
	print('Invalid identifier name....\nUsage:([a-z]+_+[A-Z])([a-z]+_+[A-Z]+[0-9])*')
	
else:
	if identifier_name not in KEYWORD_LIST:
		pass
		err_list=[]
		for i in identifier_name:
			if i not in INVALID_SPECIAL_CHARACTERS:
				pass
			else:
				err_list.append(i)
		if len(err_list)==0:
			print('Valid identifier name: Accepted')
		else:
			print('Invalid identifier name because of the following characters: ',err_list,': Rejected\nPlease remove the aboue character and try again....',sep='')
	else:
		print('Identifer name is keyword: Rejected')
												 




