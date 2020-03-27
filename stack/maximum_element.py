'''Find the maximum element in the stack 
after performing few queries
1 x  -Push the element x into the stack.
2    -Delete the element present at the top of the stack.
3    -Print the maximum element in the stack.

'''
#ProblemStatement:
#https://www.hackerrank.com/challenges/maximum-element/problem



def maximum_element_modified(n):	#saving time from finding max_element
	stack=list()
	for i in range(n):
		x,*y=tuple(map(int,input().strip().split()))
		if x==1:        stack.append(y[0])
		if x==2:        stack.pop()
		if x==3:	print(max(stack))

		


if globals()['__name__']=='__main__':
	n=int(input().strip())
	maximum_element_modified(n)
