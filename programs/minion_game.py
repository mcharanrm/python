from functools import reduce

def minion_game(s):
	ts=len(s);n=0;c=1
	while n<ts:
		i=0;j=c
		while i<ts and j<=ts:
			yield string[i:j:]
			i+=1;j+=1
		n+=1;c+=1


if globals()['__name__']=='__main__':
	string=input('Enter a string: ').strip().upper()
	result=minion_game(string)
	stuart=0;kevin=0
	for char in result:
		if char[0] not in 'AEIOU':
			stuart+=1
		else:
			kevin+=1

	if stuart==kevin:
		print('{}'.format('Draw'))
	elif stuart>kevin:
		print('{} {}'.format('Stuart',stuart))
	else:
		print('{} {}'.format('Kevin',kevin))
