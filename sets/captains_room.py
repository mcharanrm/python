#https://www.hackerrank.com/challenges/py-the-captains-room/problem

#need two sets to capture one unique captains room

if globals()['__name__']=='__main__':
	k=int(input().strip())
	rooms=map(int,input().split())
	s1=set()
	s2=set()
	for i in rooms:
		if i not in s1:
			s1.add(i)
		else:
			s2.add(i)
	key=s1.symmetric_difference(s2)
	print('{}'.format(key.pop()))

