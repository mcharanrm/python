#https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem


import itertools

if __name__=='__main__':
	s,n=input().split()
	result=itertools.combinations_with_replacement(sorted(s),eval(n))
	for item in result:
		print('{}'.format(''.join(item)))

