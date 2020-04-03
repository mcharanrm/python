#https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

if globals()['__name__']=='__main__':
	n=int(input())
	s=set(map(int, input().split()))
	ni=int(input())
	for i in range(ni):
		task=input().strip()
		if task[0]=='p':
			s.pop()
		elif task[0]=='r':
			s.remove(eval(task[-1]))
		else:
			s.discard(eval(task[-1]))
	print('{}'.format(sum(s)))


