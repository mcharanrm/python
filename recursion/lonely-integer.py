#!/usr/bin/python3.6

#https://www.hackerrank.com/challenges/lonely-integer-2/problem
from math import *

def find_lonely_integer(l):
    #perfor recursive slicing
    if len(l) >= 2:             
        si=floor(len(l)/2)
        lh=l[:si:]
        up=l[si::]
        rlh=find_lonely_integer(lh);rup=find_lonely_integer(up)
        tmp=rlh.copy()
        for i in tmp:
              if i in rup:
                   rlh.remove(i);rup.remove(i)
              else:
                   pass
        return rlh+rup
    else:
        return l 


if globals()['__name__'] == '__main__':
    N = eval(input('Enter size of the array: ').strip())
    A = list(map(int,input('Enter elements of the array: ').strip().split()))
    print('{}'.format(' '.join(list(map(str,find_lonely_integer(A))))))
