#https://www.hackerrank.com/challenges/itertools-combinations/problem

import itertools

if __name__=='__main__':
	s,n=input().split()
	counter=1
	while counter<=eval(n):
		result=itertools.combinations(sorted(s),counter)
		for item in result:
		print('{}'.format(''.join(item)))
		counter+=1

