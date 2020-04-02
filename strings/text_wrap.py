#wrap the strings s into paragraph of width w
#https://www.hackerrank.com/challenges/text-wrap/problem

def wrap_text(string,max_width):
	n=len(string)
	q,r=divmod(n,max_width)
	i=0;j=max_width;counter=0
	if r!=0:
		pass
		q+=1
		
	while counter<q:
		print(string[i:j:])
		i+=max_width;j+=max_width
		counter+=1

if __name__=='__main__':
	string,max_width=input('Enter your string: ').strip(),int(input('Enter max_width: ').strip())
	wrap_text(string,max_width)

