#!/usr/bin/python3.6

#https://www.hackerrank.com/challenges/input/problem

if globals()['__name__']=='__main__':
    #list unpacking
    x,k=map(eval,input().split())
    #substitue x in polynomial equation
    result=eval(input())
    if result==k:
        print('{}'.format('True'))
    else:
        print('{}'.format('False'))
