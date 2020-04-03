#https://www.hackerrank.com/challenges/python-quest-1/problem

'''Condition: More than 2 lines will result in 0 score. Do not leave a blank line also
1
22
333
4444

Steps:
	1(10**0)	 2*(10**1)+2(10**0)	3*(10**2)+3(10**1)+3(10**0)	4*(10**3)+4(10**2)+4(10**1)+4(10**0)
						3(100+10+1)
						numbers are in GP
						sum.no.gp is  a*(r**n-1)//r-1
'''

for i in range(1,int(input())):
#	print('{}'.format(str(i)*i))    #not-allowed	
#	print('{}'.format(sum([ i*(10**(x)) for x in range(i)])))   #not-allowed
#	print('{}'.format(sum(list(map(lambda x: i*(10**(x)),range(i))))))  #not-allowed
#	print('{}'.format(i*((10**i-1)//9)))	#VALID
	print((i*((10**i-1)//9)))	#VALID
