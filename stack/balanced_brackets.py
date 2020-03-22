#ProblemStatement:
#https://www.hackerrank.com/challenges/balanced-brackets/problem


'''Check if the string is balanced or not.
All chracters in the sequences ∈ {, }, (, ), [, ] 
For each string, return YES or NO'''

'''Sample Input:
3
{[()]}
{[(])}
{{[[(())]]}} 

Sample Output:
YES
NO
YES'''

#Globals()
valid_push_strings=list('{([')
valid_pop_strings=list('])}')
stack=list()

def isBalanced(s):
	if len(s)%2!=0:
		return 'NO'
	else:
		m=len(s)//2
		try:
			if s[:1:] in valid_push_strings:
				for schar in s[::]:
					if schar in valid_push_strings:
						stack.append(schar)
					else:
						if stack[-1]=='(' and schar==')':
							stack.pop()
						elif stack[-1]=='{' and schar=='}':
							stack.pop()
						elif stack[-1]=='[' and schar==']':
							stack.pop()
						else:
							return 'NO'
				return 'YES'
			else:
				return 'NO'
		except IndexError:
			return 'NO'


#input()
if __name__=='__main__':
	n=int(input('Enter no.of strings: ').strip())
	for i in range(n):
		s=input('enter your string: ')
		result=isBalanced(s)
		print(result)

