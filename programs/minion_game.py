#string='abcd'
'''
abc		abcd	(n*(n+1))/2 - proper substrings. #no.of times a user can participate 

a,b,c		a,b,c,d
ab,bc,ca	ab,bc,cd
abc		abc,bcd
		abcd

Approach:			1 	2 	3 	4 
				4ti	3ti	2ti	1ti

			n=1
                        while n<=len(string):
                                i=0;j=n;k=0
                                while k<len(string) and j>len(string)
                                        s=''
1-L                                     for i in string[i:j:]:
                                                if len(string[i:j+1:])==1:      array.append(i)
slicing [0:1:]                                  if len(string[i:j+1:])>1:       s+=i    
        [1:2:]                          i+=1;j+=1;k+=1
        [2:3:]                  n+=1
	[3:4:]
2-L
slicing [0:2:]
	[1:3:]
	[2:4:]
	[3:5:] invalid

3-L
slicing	[0:3:]
	[1:4:]
	[2:5:] invalid
	[3:6:]

4-L
slicing	[0:4:]
	[1:5:] invalid
	[2:6:]
'''
#n=0;c=2;array=list();array.extend(string)
from functools import reduce


def game_minion_substrings():
        c_array=list();v_array=list()
        n=0;c=2;array.extend(string)
        while n<len(string):
                i=0;j=c
                while i<len(string) and j<=len(string):
                        array.append(''.join(string[i:j:]))
                        i+=1;j+=1
                n+=1;c+=1
        v_array=[x for x in array if x[0] in list('AEIOU')]
        c_array=[x for x in array if x[0] not in  list('AEIOU')]
        if len(v_array)==len(c_array):
                print('{}'.format('Draw'))
        elif len(v_array)>len(c_array):
                print('{} {}'.format('Kevin',len(v_array)))
        else:
                print('{} {}'.format('Stuart',len(c_array)))


def game_minion(string):
	n=0;c=2;array.extend(string)
	while n<len(string):
		i=0;j=c;k=0
		while k<len(string) and j<=len(string):
			s=''
			for char in string[i:j:]:
				s=s+char
			array.append(s)
			i+=1;j+=1;k+=1
		n+=1;c+=1


def game_multiuser_play():
	n=len(array);i=0;p1_score_array=list();p2_score_array=list()
	p1_taken=list();p2_taken=list()		#what if repeated substrings entered
	print('{}{}{}{}'.format(' '.center(20),p_1.center(40),p_2.center(40),'LEAD'.center(40)))
	print('{}{}{}'.format(' '.center(20),'word'.center(20),'score'.center(20)),end=' ')
	print('{}{}'.format('word'.center(20),'score'.center(20)))
	print("{}{}".format(' '.center(20),'  '.center(90,"-")),end=' ')
	print(" {}".format("".center(30,"-")))
	while i<n:
		p1=input('{} turn: '.format(p_1.lower())).strip().upper()
		p2=input('{} turn: '.format(p_2.lower())).strip().upper()
		print('{}{}{}'.format(' '.center(20),p1.center(20),str(array.count(p1)).center(20)),end=' ')
		print('{}{}'.format(p2.center(20),str(array.count(p2)).center(20)),end=' ')
		p1_score_array.append(array.count(p1));p2_score_array.append(array.count(p2))
		p1_score=0;p2_score=0
		for j in range(len(p1_score_array)):
			p1_score+=p1_score_array[j]
		for j in range(len(p2_score_array)):
			p2_score+=p2_score_array[j]
		i+=1
		if p1_score==n:
			print('{}'.format(('WINNER-'+p_1).center(40)))
			break
		elif p2_score==n:
			print('{}'.format(('WINNER-'+p_2).center(40)))
			break
		elif p1_score==p2_score:
			print('{}'.format('DRAW'.center(40)))
		elif p1_score<p2_score:
			print('{}'.format(p_2.center(40)))
		else:
			print('{}'.format(p_1.center(40)))
		
if globals()['__name__']=='__main__':
	array=list()
#	p_1=input('Enter player name: ').strip().upper()
#	p_2=input('Enter player-2 name: ').strip().upper()
	string=input('Enter a string: ').strip().upper()
	game_minion_substrings()
#	game_singleuser_play()
#	game_multiuser_play()	
