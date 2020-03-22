#display perfect squares present in the range of i/p

from math import ceil,floor
l,h=(eval(x) for x in input('Enter your lower and upper range to display valid perfect square roots: ').split())

def perfectsquares(x=1,y=100):
	if x<y:
		lower=floor(x**(0.5))
		higer=ceil(y**(0.5))
		for i in range(lower,higer+1):
			n=i**2
			if n>=x and n<=y:
				print(n)
	else:
		print('Lower bound should not be greater than or equal to upper bound')

perfectsquares(x=l,y=h)

	
