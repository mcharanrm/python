#https://www.hackerrank.com/challenges/equal-stacks/problem


def equalStacks(h1,h2,h3):
	s1=sum(h1)
	s2=sum(h2)
	s3=sum(h3)
	if s1<s2 and s1<s3:
		max_height=s1
	elif s2<s1 and s2<s3:
		max_height=s2
	else:
		max_height=s3
	while max_height != s1 or max_height != s2 or max_height != s3:
		while s1>max_height:
			s1_ret=h1.pop()
			s1=s1-s1_ret
		max_height=s1
		while s2>max_height:
			s2_ret=h2.pop()
			s2=s2-s2_ret
		max_height=s2
		while s3>max_height:
			s3_ret=h3.pop()
			s3=s3-s3_ret
		max_height=s3
	return max_height
	


if __name__=='__main__':
	n1,n2,n3=tuple(map(int,input('Enter size of 3 stacks: ').strip().split()))
	h1=[int(x) for x in input('Enter stack 1 cylinders: ').strip().split()[::-1]]
	h2=[int(x) for x in input('Enter stack 2 cylinders: ').strip().split()[::-1]]
	h3=[int(x) for x in input('Enter stack 3 cylinders: ').strip().split()[::-1]]
	max_height=equalStacks(h1,h2,h3)
	print(max_height)
