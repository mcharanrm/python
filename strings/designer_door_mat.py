#https://www.hackerrank.com/challenges/designer-door-mat/problem

from math import floor


def design_door_mat(N,M):
	design='.|.'
	for i in range(floor(N/2)):
		print('{}'.format(((design*(i*2))+design).center(M,'-')))
	print('{}'.format('WELCOME'.center(M,'-')))
	for i in range((floor(N/2)-1),-1,-1):
		print('{}'.format(((design*(i*2))+design).center(M,'-')))



if globals()['__name__']=='__main__':
	N,M=tuple(map(int,input('Enter values of N and M for design: ').strip().split()))
	design_door_mat(N,M)
