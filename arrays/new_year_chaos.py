#https://www.hackerrank.com/challenges/new-year-chaos/problem

'''test-case:
1 2 5 3 7 8 6 4		#Input

steps:
1 2 3 5 7 8 6 4 	#swaps=1
1 2 3 5 7 6 4 8		#swaps=3
1 2 3 5 6 4 7 8		#swaps=5
1 2 3 5 4 6 7 8 	#swaps=6
1 2 3 4 5 6 7 8 	#swaps=7	#optimal swaps=7
'''


def minimumBribes(n,array):
	k=0;swap=0
	while k<n:
		for i in range(n):
			if array[i] == i+1:
				pass
			else:
				j=i
				key=array[j]
				tmp=0
				while j+1<n and key>array[j+1]:
					array[j]=array[j+1]
					j+=1
					tmp+=1
				array[j]=key
				if tmp<=2:	swap+=tmp
				if tmp>2:	return 'Too chaotic'
		k+=1
	return swap

				

if globals()['__name__']=='__main__':
	test_cases=int(input('enter no.of test cases: ').strip())
	for i in range(test_cases):
		array_size=int(input('Enter array size: ').strip())
		array=list(map(int,input('Enter array elements: ').strip().split()))
		result=minimumBribes(array_size,array)
		print(result)

