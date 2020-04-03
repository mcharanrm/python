#https://www.hackerrank.com/challenges/symmetric-difference/problem


def symmetric_difference():
	N=int(input().strip())
	s1=set(map(int,input().strip().split()))
	M=int(input().strip())
	s2=set(map(int,input().strip().split()))
	return sorted(s1.symmetric_difference(s2))





if globals()['__name__']=='__main__':
	S=symmetric_difference()
	for i in S:
		print(i)

