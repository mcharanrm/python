#https://www.hackerrank.com/challenges/iterables-and-iterators/problem

from itertools import combinations

if __name__=='__main__':
	n=int(input())  #length of the string
	s=input().split()   #list of alphabets
	k=int(input())  #required length of string combinations 
	counter=0
	valid=0
	result=combinations(s,k)
	for item in result:
		if item.count('a')>=1:
			valid+=1
		counter+=1
	print('{:0.3f}'.format(valid/counter))	#probability of occurrence of 'a' in total combinations

