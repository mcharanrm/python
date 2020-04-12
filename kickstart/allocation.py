#https://codingcompetitions.withgoogle.com/kickstart/


if __name__=='__main__':
	T=int(input().strip())		#total test cases
	result=list()
	for i in range(T):
		N,B=list(map(int,input().strip().split()))	#no.of houses and budget
		array=sorted(map(int,input().strip().split()))	#price of each house  #sum,sorted can be used along with generator functions
		count=0
		price=0
		for item in array:
			price+=item
			if price<=B:
				count+=1
			else:
				break
		result.append(count)

	#below two procedures potentially yeilds the same result

	inc=1	#Test case incrementing value
	for item in result:
		print('Case #{}: {}'.format(inc,item))
		inc+=1
	print()

	#other work around if we don't want value incr each time
	items=result.__iter__()	#created iterator for result
	for item in range(1,(T+1)):
		print('Case #{}: {}'.format(item,next(items)))

