#ProblemStatement
#https://www.hackerrank.com/challenges/array-left-rotation/problem

'''
n=5 6 7 8 9, r=3
  0 1 2 3 4

r-1: a[0]=key	
	
     a[0]=a[1]	a[i]=a[i+1]
     a[1]=a[2]	
     a[2]=a[3]	
     a[3]=a[4]	a[3]=a[3+1]
		a[4]=a[4+1] -->invalid, break the loop

'''
def left_rotation(n,r):
	array=list(map(int,input().strip().split()))
	counter=0	
	while counter<r:
		index=0
		key=array[index]
		while index<(n-1):
			array[index]=array[index+1]
			index+=1
		array[index]=key
		counter+=1

	print(array)

def left_rotation_modified(n,r):
	array=list(map(int,input().strip().split()))
	array=array[r::]+array[:r:]     #without loop
	print(array)


if globals()['__name__']=='__main__':
	n,r=tuple(map(int,input().strip().split()))
	left_rotation_modified(n,r)
