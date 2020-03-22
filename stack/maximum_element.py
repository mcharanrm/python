'''Find the maximum element in the stack 
after performing few queries
1 x  -Push the element x into the stack.
2    -Delete the element present at the top of the stack.
3    -Print the maximum element in the stack.

'''
#ProblemStatement:
#https://www.hackerrank.com/challenges/maximum-element/problem


def maximum_element(n):
	array=list()
	array_op=list()
	for i in range(n):
		x,*y=tuple(map(int,input().strip().split()))
		if x==1:	array.append(y[0])
		if x==2:	array.pop()
		if x==3:
			max_e=array[0]
			for j in array:
				if max_e<j:	max_e=j
			array_op.append(max_e)

	for i in array_op:
		print(i)	


def maximum_element_modified(n):	#saving time from finding max_element
	array=list()
	array_op=list()
	for i in range(n):
		x,*y=tuple(map(int,input().strip().split()))
		if x==1:        array.append(y[0])
		if x==2:        array.pop()
		if x==3:	tmp=array.copy();tmp.sort(reverse=True);array_op.append(tmp[0])

	for i in array_op:
		print(i)

		


if globals()['__name__']=='__main__':
	n=int(input().strip())
	maximum_element_modified(n)
