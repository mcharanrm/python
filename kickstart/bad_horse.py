#https://code.google.com/codejam/contest/2933486/dashboard
#small data set 1<=M<=10 T=testcases ; M=no.of lines

#Whole problem is depends on biparted graph [a subset of undirted graph, A->B == B->A]


def cycle_detection():
	tmp=set()
	for item in tp:
		if db[item][0] == -1:
			db[item][0]=1
			for i in db[item][1::]:
				db[i][0]=0
				tmp.add(i)
		elif db[item][0] == 0 and item in tmp:
			pass
			db[item][0]=1
			tmp.discard(item)
			for i in db[item][1::]:
				if db[i][0] == 1:
					pass
				elif db[i][0] == 0 and i in tmp:
					return 'No'
				elif db[i][0] == -1:
					tmp.add(i)
					db[i][0]=0
	return "Yes"
					
			

def even_odd_cycle_detection():
	#if the degree is 2 then it is eligible for cycle 
	#odd length cycles are not part of biparted graph
	#even length cycles are part of biparted graph
	counter=0
	for person in tp:
		if len(db[person]) == 2:
			pass
			counter+=1
		else:
			return 'No'
	if counter == N and N%2 == 0:
		return 'Yes'
	else:
		return 'No'
		

if globals()['__name__']=='__main__':
	T=int(input())
	for i in range(T):
		pass
		M=int(input())
		db=dict()	#to find no.of edges for each person
		tp=set()	#total people
		for j in range(M):
			a,b=input().strip().split()
			if a not in db.keys() :
				db[a]=list()
				db[a].append(-1)
				db[a].append(b)
			else:
				db[a].append(b)
			if b not in db.keys() :
				db[b]=list()
				db[b].append(-1)
				db[b].append(a)
			else:
				db[b].append(a)     #undirected grap
			tp.add(a);tp.add(b)         #to find unique members
		N=len(tp)
		m,n=divmod(N,2)
		max_edges=(m*(m+n))		    #max possible edges in a biparted graph
		if M > max_edges:
			print('Case #{}: {}'.format((i+1),'No'))
		else:
			result=cycle_detection()
			if result == 'Yes':				
				print('Case #{}: {}'.format((i+1),result))
			elif N == M and result == 'N0':
				print('Case #{}: {}'.format((i+1),even_odd_cycle_detection()))
			else:
				print('Case #{}: {}'.format((i+1),result))
