#insertion Sort

def insertion_sort():
	a=[eval(x) for x in input('Please enter your list of numbers seperated by space: ').split()]
	for j in range(1,len(a)):
		key=a[j]
		#Insert a[j] into the sorted sequence a[0....j-1]
		i=j-1
		while i>=0 and a[i]>key:		#2 3 5 1 6
			a[i+1]=a[i]			#1 2 3 5    
			i-=1
		a[i+1]=key
	print('Sorted order of elements are: ',a)




		
if globals()['__name__']=='__main__':		
	insertion_sort()
	
