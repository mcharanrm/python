#https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
#0<N<=100


def distinct_heights_method_1():
	N=int(input().strip())
	S={eval(x) for x in input().strip().split()}	#set comprehension
	print('{}'.format(sum(S)/len(S)))


def distinct_heights_method_2():
	N=int(input().strip())
	S=set(map(int,input().strip().split()))		#using map and type conversion
	print('{}'.format(sum(S)/len(S)))

def average(array):
	S={x for x in array}
	return (sum(S)/len(S))




if globals()['__name__']=='__main__':
	n=int(input())
	arr=map(int,input().split())	#arr is generator object
	result=average(arr)
	print(result)

