#https://codingcompetitions.withgoogle.com/kickstart/round/


if __name__=='__main__':
	T=int(input())		#no.of test cases
	result=list()
	for i in range(T):
		N,K,P=list(map(int,input().split()))	#no.of stacks,no.of values in stack,no.of plates to pick
		tmp=list()	#to hold stack values
		for j in range(N):
			values=list(map(int,input().split()))
			tmp+=[values]	#creating nested lists
		#use while as main loop to pick 'P' plates from stack
		#use for as sub loop to read over all the lists
		counter=0
		score=0
		while counter<P:	#to pick P plates
			beauty=0
			loc=0		#location;to identify which nested list holding maximum value
			for j in range(N):	#iterating over N nested lists
				if len(tmp[j])!=0 and beauty<tmp[j][0]:
					pass
					beauty=tmp[j][0]
					loc=j
			score+=beauty
			#tmp.remove(tmp[loc][-1])	#since we read it,remove it #failing because it is nested, remove works on normal list
			tmp[loc].remove(tmp[loc][0])   #pop() can also be used
			counter+=1
		result.append(score)
	#loop over result for final o/p
	items=result.__iter__()
	for item in range(1,(T+1)):
		print('Case #{}: {}'.format(item,next(items)))			
