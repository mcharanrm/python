#ProblemStatement:
#https://www.hackerrank.com/challenges/arrays-ds/problem

n=int(input('number elements in the list: '))
array=list(map(int,input('array elements: ').strip().split()))


#using for loop
def reverse_list_f(array):
	for i in array[::-1]:
		print(i,end=' ')

#using while loop
def reverse_list_w(array):
	counter=n-1
	while counter>=0:
		print(array[counter],end=' ')
		counter-=1



