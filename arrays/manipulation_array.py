#ProbelmStatement
#https://www.hackerrank.com/challenges/crush/problem


def array_manipulation(n,q):
	array=list()
	string_of_zeros='0'*n	#string repeation
	array=list(map(int,string_of_zeros))
	for i in range(q):	#taking 2 dimensional array input
		query=(list(map(int,input().strip().split())))
		a,b,k=query
		array=array[:(a-1):]+list(map((lambda x:x+k),array[(a-1):b:]))+array[b::]
		
	array.sort(reverse=True)
	print('the max element is: {}'.format(array[0]))
		


if globals()['__name__']=='__main__':
	n,q=tuple(map(int,input('enter n and q: ').strip().split()))
	array_manipulation(n,q)
