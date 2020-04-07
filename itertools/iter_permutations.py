#https://www.hackerrank.com/challenges/itertools-permutations/problem

import itertools

if __name__=='__main__':
	s,n=input().split()
	result=itertools.permutations(sorted(s),eval(n))
	for item in result:
		print('{}'.format(''.join(item)))


