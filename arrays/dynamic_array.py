#ProblemStatement:
#https://www.hackerrank.com/challenges/dynamic-array/problem

def dynamic_array(n,q):
	query=list()
	for i in range(q):	
		query.append(list(map(int,input('enter your querys:').strip().split())))
	d=dict()	#to save seq lists
	t=tuple(map((lambda x:'s'+str(x)),range(n)))
	for i in t:
		d[i]=list()
	#accessing query and solving sub problems
	lastAnswer=0
	for i in query:
		qn,x,y=i
		if qn==1:
			s_l='s'+str(((x^lastAnswer)%n))
			d[s_l].append(y)
		elif qn==2:
			s_l='s'+str(((x^lastAnswer)%n))
			lastAnswer=(d[s_l][(y%len(d[s_l]))])
			print(lastAnswer)
			

if __name__=='__main__':
	n,q=tuple(map(int,input('Enter n and q: ').strip().split()))
	dynamic_array(n,q)

