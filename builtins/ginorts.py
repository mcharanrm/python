#!/usr/bin/python3.6

#https://www.hackerrank.com/challenges/ginorts/problem

if __name__ == '__main__':
    user_input=input()
    lower_items='';upper_items='';odd_items='';even_items=''
    for item in user_input:
        if item.islower():
            lower_items=lower_items+item
        elif item.isupper():
            upper_items=upper_items+item
        else:
            if eval(item)%2 != 0:
                odd_items=odd_items+item
            else:
                even_items=even_items+item
    result=sorted(lower_items)+sorted(upper_items)+sorted(odd_items)+sorted(even_items)
    print('{}'.format(''.join(result)))
    
