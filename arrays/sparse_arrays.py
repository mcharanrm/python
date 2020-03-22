#ProblemStatement:
#https://www.hackerrank.com/challenges/sparse-arrays/problem

'''There is a collection of input strings and a collection of query strings. 
For each query string, determine how many times it occurs in the list of input strings

Approach:
1.count() - check occurrences
	    takes only one argument,since it is list.method
	    if it is string method, takes atleast-1, atmost-3
'''



def sparse_array():
	a_strings=list()
	q_strings=list()
	no_a=int(input().strip())
	for i in range(no_a):
		a_strings.append(input().strip())
	no_q=int(input().strip())
	for i in range(no_q):
		q_strings.append(a_strings.count(input().strip()))
	for i in q_strings[::]:
		print(i)
		



if globals()['__name__']=='__main__':
	sparse_array()
