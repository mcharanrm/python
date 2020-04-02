#https://www.hackerrank.com/challenges/alphabet-rangoli/problem
'''						
							3
considered:					3	2	3
					3	2	1	2	3
						3	2	3
1. 3,2[diff is -1] 2,3 [diff is +1]			3
2. used two while loops for decrement and increment
3. 0 to n used 1-for loop
4. n-1 to 0 used for 2-for loop	'''


def print_rangoli(n):
	numbers=list(range(1,27))
	alphabets=list('abcdefghijklmnopqrstuvwxyz')
	db=dict(zip(numbers,alphabets))
	width=((n+(n-1))+((n+(n-1))-1))
	for i in range(n):
		s=''
		j=n
		while j>=(n-i):
			s+=db[j]
			j-=1
		j=n-i
		while j<n:
			j+=1
			s+=db[j]
		print('{}'.format(('-'.join(s)).center(width,'-')))
	k=n-2
	for i in range(k,-1,-1):
		s=''
		j=n
		while j>=(n-i):
			s+=db[j]
			j-=1
		j=n-i
		while j<n:
			j+=1
			s+=db[j]
		print('{}'.format(('-'.join(s)).center(width,'-')))
	

if globals()['__name__']=='__main__':
	size=int(input('Enter size of the Rangoli: ').strip())
	print_rangoli(size)
	
