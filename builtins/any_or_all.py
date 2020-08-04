#!/usr/bin/python3.6

#https://www.hackerrank.com/challenges/any-or-all/problem


def find_positive_integers(x):
    if x <= 0:
        return False
    else:
        return True

def find_palidrome_numbers(x):
    q,r=divmod(len(str(x)),2)   #1,3,5 are odd-length and 2,4,6 or even-length
    if r == 0:
        if str(x)[:len(str(x))//2:] == str(x)[len(str(x))-1:len(str(x))//2-1:-1]:
            return True
        else:
            return False
    else:
        if str(x)[:len(str(x))//2:] == str(x)[len(str(x))-1:len(str(x))//2:-1]:
            return True
        else:
            return False



if __name__ == '__main__':
    #read the values from stdin
    n=input()
    values=list(map(eval,input().split()))
    result_positive_integers=list(map(find_positive_integers,values))
    if all(result_positive_integers):
        result_palindromes=list(map(find_palidrome_numbers,values))
        if any(result_palindromes):
            print('{}'.format('True'))
        else:
            print('{}'.format('False'))
    else:
        print('{}'.format('False'))
