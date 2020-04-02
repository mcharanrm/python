#https://www.hackerrank.com/challenges/capitalize/problem

def solve(s):
	scount=s.count(' ')
	n=0
	i=0
	l=len(s)
	tmp=[]
	if scount:
		while n<scount:
			sindex=s.find(' ',i,l)
			if sindex!=i:
				tmp.append(s[i:sindex:].capitalize())
				i=sindex+1
				tmp.append(s[sindex:i:])
			else:
				i=sindex+1
				tmp.append(s[sindex:i:])
					
			n+=1
		tmp.append(s[i::].capitalize())
		print('{}'.format(''.join(tmp)))
			
	else:
		print('{}'.format(s.capitalize()))



if __name__=='__main__':
	s=input('Enter a String: ')
	solve(s)
