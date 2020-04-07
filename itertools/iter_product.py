#https://www.hackerrank.com/challenges/itertools-product/problem

import itertools

if __name__=='__main__':
	a=list(map(int,input().split()))
	b=list(map(int,input().split()))
	result=itertools.product(a,b)
	for item in result:
		print(item,end=' ')
