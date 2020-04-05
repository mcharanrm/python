#https://www.hackerrank.com/challenges/polar-coordinates/problem

'''points:
1.Similar to cartesian plane but difference is, co-ordinates are represented
  using radius and angle.
2.Complex numbers can be used to find the polar co-ordinates.
3.Z=r(cosT+JsinT) Z=a+bj a=rcosT; b=rsinT and tanT=b/a;T=atan(b/a)'''

from math import acos,sqrt

if __name__=='__main__':
    c=eval(input()) 		#complex number
    r=(sqrt(pow(c.real,2)+pow(c.imag,2)))	#radius=distance b/w origin and location of complex number in polar co-orinate system
    i=acos(c.real/r)		#to find angle. sin(t)=a/c, cos(t)=b/c and tan(c)=a/b; height=a;base=b;hypotenuse=c ;see angle-problem
    if str(c.real)[0]=='-' and str(c.imag)[0]=='-':	#clock-wise = -ve
        print('{:0.3f}\n{:0.3f}'.format(r,(-i)))
    elif str(c.imag)[0]=='-':
        print('{:0.3f}\n{:0.3f}'.format(r,(-i)))	#clock-wise = -ve
    else:
        print('{:0.3f}\n{:0.3f}'.format(r,i))		#counter-clock = +ve


