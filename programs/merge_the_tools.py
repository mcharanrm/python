#https://www.hackerrank.com/challenges/merge-the-tools/problem


def merge_tools(s,k):
	def merge_work(s,k):
		n=len(s)
		ti=n//k		#no.of times either for or while loop has to execute
		for l in range(ti):
			sub_string=s[(k*l):(k*(l+1)):]
			i=0;j=0
			tmp=''
			while i<k-1:
				j=i+1
				while j<k:
					if sub_string[i]!=sub_string[j]:
						j+=1
					else:
						break
				if j==k:
					pass
					tmp+=sub_string[i]
				i+=1

			tmp+=sub_string[i]
			yield tmp
	merge_work(s,k)
	result=merge_work(s,k)
	for valid_strings in result:
		print(valid_strings)



if globals()['__name__']=='__main__':
	string=input('Enter input string: ').strip()
	segment=int(input('Enter subsegement size: ').strip())
	merge_tools(string,segment)
