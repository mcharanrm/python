#https://www.hackerrank.com/challenges/py-check-strict-superset/problem


def strict_superset(sa,n):	
	for i in range(n):
		ss=set(map(int,input().split()))	#provided subset
		dsa=len(sa.difference(ss))
		dss=len(ss.difference(sa))
		if dsa==0 or dss!=0:
			return False
		elif dsa==0 and dss==0:
			return False
	return True


if __name__=='__main__':
	sa=set(map(int,input().split()))                #given superset
	n=int(input())
	print('{}'.format(strict_superset(sa,n)))

