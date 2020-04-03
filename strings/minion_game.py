#https://www.hackerrank.com/challenges/the-minion-game/problem

'''
Previous: 
1.Instead of going for all possible sub_strings over a given string and counting them for each user is time taking process
2.If string length increases then strings possible over given string increases exponentially
Eg:
	string 		len-of-string total-substrings
	abc		3		6
	abcd		4		10
	abcde		5		15
	abcdefghij	10		55
**So looping over them is diffucul**

Now:
1.from length of the string we can find the total possible substrings
2.we calculate no.of possible sub strings for either Stuart or Kevin
3.But it suggested to go for Vowels(Kevin), less membership comparisions
4.if index of elment is 0, then possible substrings with respect to that perticular element \
  is (n-i)

Eg:	abc	a(a,ab,abc)		b(b,bc)		c(c)
		index=0;3-0=3	     index=1;3-1=2    index=2;3-2=1 '''

def minion_game(s):
	n=len(s)	#length of the string
	ts=(n*(n+1))//2	#Total possible sub_strings
	Kevin=0
	Stuart=0
	for i in range(n):
		if s[i] in 'AEIOU':
			Kevin+=(n-i)
	Stuart=ts-Kevin
	if Stuart==Kevin:	print('Draw')
	if Stuart>Kevin:	print('Stuart {}'.format(Stuart))
	if Stuart<Kevin:	print('Kevin {}'.format(Kevin))
	

if globals()['__name__']=='__main__':
	s=input()
	minion_game(s)



