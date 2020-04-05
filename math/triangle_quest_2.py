#https://www.hackerrank.com/challenges/triangle-quest-2/problem

#this may not be great because it took me 3 hours to come finish this problem

'''Problem: Palindromic Triangle
1
121
12321
1234321
123454321

Conditions:
1.You can't take more than two lines
2.You have to complete the code using exactly one print statement.
3.Using anything related to strings will give a score of 0
4.Using more than one for-statement will give a score of 0


Steps:
1.expand each number using base10 [eg: 121 - 1*(10**2)+2*(10**1)+1*(10**0)]
2.take one even and odd values of i to understand the expression [i=3,i=4]
3.expand 3rd and 4th values given in triangle sequence 
	i=3							i=4
	1*(10**4)+2*(10**3)+3*(10**2)+2*(10**1)+1*(10**0)	1*(10**6)+2*(10**5)+3*(10**4)+4*(10**3)+3*(10**2)+2*(10**1)+1*(10**0)

4.simplify expression even further [eg: 2*(10**1) == 20 == (10**1) + (10**1)]
5.Write in a colum-major order to understand	[ All terms in Geometri Progression ] [ sum of n-terms An=a*(r**n - 1)  ]
													  ------------
													     r-1

	10**4 +							10**6
	10**3 + 10**3						10**5 + 10**5
	10**2 + 10**2 + 10**2					10**4 + 10**4 + 10**4
	10**1 + 10**1						10**3 + 10**3 + 10**3 + 10**3
	10**0							10**2 + 10**2 + 10**2
								10**1 + 10**1
								10**0

6.solving expression would look like this 
	1*(10**5 - 1)  10*(10**3 - 1) 				1*(10**7 - 1)    10*(10**5 - 1)     10**2(10**3 - 1)
	----------   + -------------  + 10**2			------------- +  -------------- +  ----------------- + 10**3
	   10-1		  10-1					     10-1           10-1                10-1

7.expand the expression and simplify it.
	(10**5 + 10**4) - (1 + 10) 				(10**7+10**6+10**5) - (1+10+10**2)
	--------------    -------- + 10**2			-------------------   ------------ + 10**3
	    9		    9						9		   9

8. After solving and writing general-expression would look like this
	(10**(i-1) - 1)[10**(i+1) -1] 
	----------------------------- + 10**(i-1)
		9*9
'''

#program wrt to given problem

for i in range(1,int(input())+1):
	print ((((10**(i-1)-1)*(10**(i+1)-1))//81)+(10**(i-1)))




