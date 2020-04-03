#https://www.hackerrank.com/challenges/py-check-subset/problem


if __name__=='__main__':
	t=int(input())
	for i in range(t):
		an=int(input())
		a=set(map(int,input().split()))
		bn=int(input())
		b=set(map(int,input().split()))
		da=len(a.difference(b))
		if da==0:	print(True)
		if da!=0:	print(False)

	
