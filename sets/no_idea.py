#https://www.hackerrank.com/challenges/no-idea/problem


if globals()['__name__']=='__main__':
	n,m=tuple(map(int,input().split()))
	array=map(int,input().split())
	s1=set(map(int,input().split()))
	s2=set(map(int,input().split()))
	happiness=0
	for i in array:
		if i in s1:
			happiness+=1
		elif i in s2:
			happiness+=-1
		else:
			happiness+=0
	print('{}'.format(happiness))

	
