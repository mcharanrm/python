#https://www.hackerrank.com/challenges/python-string-formatting/problem


def string_formatting(n):
	width=len(bin(n)[1::])	#return type of bin,oct,hex is always str type
	for i in range(1,(n+1),1):
		print('{}{}{}{}'.format(str(i).rjust(width-1),oct(i)[2::].rjust(width),hex(i)[2::].upper().rjust(width),bin(i)[2::].rjust(width)))
	
if __name__=='__main__':
	n=int(input('Enter a integer: '))
	string_formatting(n)	

