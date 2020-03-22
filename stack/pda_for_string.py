'''A string is formed over the given alphabets sigma=(a,b) \
  such that no.of a's are equal to no.of b's'''

#approach=stack [use list ds]

word=input('Enter your string with combinations of a and b: ').lower()
stack=list()

def pda_check(string):
	if string[0]=='a':
		try:
			for alphabet in string:
				if alphabet=='a':
					stack.append(alphabet)
				else:
					stack.pop()
		except IndexError:
			print('No.of b\'s present in the string are more than a\'s')
		else:
			if len(stack)==0:
				print('no.of a\'s and no.of b\'s are equal')
			else:
				print('no.of a\'s are greater than b\'s')
		finally:
			print('Code executed successfully')

		
	else:
		try:
			for alphabet in string:
				if alphabet=='b':
					stack.append(alphabet)
				else:
					stack.pop()
		except IndexError:
			print('No.of a\'s are greater than no.of b\'s')
		else:
			if len(stack)==0:
				print('no.of a\'s and no.of b\'s are equal')
			else:
				print('no.of b\'s are greater than a\'s')
		finally:
			print('Code executed successfully')



pda_check(word)



