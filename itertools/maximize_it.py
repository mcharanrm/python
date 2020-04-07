#https://www.hackerrank.com/challenges/maximize-it/problem

import itertools	


if __name__=='__main__':
	k,m=list(map(int,input().split()))
	smax=0
	array=list()
	for i in range(k):
		a,*b=list(map(int,input().split()))
		array=array+[b]
	result=itertools.product(*array)	#to spread out nested array as argument to cartesian-product
	for item in result:
		s=sum(map(pow,item,itertools.repeat(2)))
		smod=s%m
		if smax<smod:	smax=smod
	print(smax)
		
