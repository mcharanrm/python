#https://www.hackerrank.com/challenges/game-of-two-stacks/problem
'''Points
1.B/w two stacks look for smallest integer
2.pop
3.increment no.of popped values
4.compare sum of pop values to x
5.if sum < x: repeat '''



def twoStacks(x,a,b):
	n_a=n-1
	n_b=m-1
	pop_sum=0
	tot_integers=0
	while n_a != -1 or n_b != -1:
		if pop_sum < x:
			if a[n_a]<b[n_b]:
				a_ret=a.pop()
				pop_sum+=a_ret
				if pop_sum < x:
					n_a-=1
					tot_integers+=1
				else:
					break
			else:
				b_ret=b.pop()
				pop_sum+=b_ret
				if pop_sum < x:
					n_b-=1
					tot_integers+=1
				else:
					break
	print(tot_integers)				


if __name__=='__main__':
	g=int(input('Enter no.of games: '))
	for g_itr in range(g):
		n,m,x=list(map(int,input('Enter sizes of stacks followed by max_element: ').strip().split()))
		a=[int(i) for i in input('Enter elements of stack-1: ').strip().split()[::-1]]
		b=[int(i) for i in input('Enter elements of stack-2: ').strip().split()[::-1]]
		result=twoStacks(x,a,b)
		print(result)
	
