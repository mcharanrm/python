#Binary Search

'''Requirements:
1.binary seach works on a sorted list
2.Recursion '''

def merge_sort(n):
	if len(n)==1:
		pass
		return n
	else:	
		p=len(n)
		q=len(n)//2
		y=n[:q:]
		z=n[q::]
		a=merge_sort(y);b=merge_sort(z)
		m_list=[]
		i=0;j=0
		while i<len(a) and j<len(b):
			if a[i]<b[j]:
				m_list.append(a[i])
				i+=1
				if i==len(a):	#person responsible for loop break has to add other members to the sorted list
					m_list.extend([b[k] for k in range(j,len(b))])	#list comprehension technique and extend() attribute
			else:
				m_list.append(b[j])
				j+=1
				if j==len(b):	#person responsible for loop break has to add other members to the sorted list
					m_list.extend([a[k] for k in range(i,len(a))])	##list comprehension technique and extend() attribute
		return m_list

def binary_search(s):
	if len(s)==1 and T==s[0]:
		pass
		print('Search target is found: ',T)
	elif len(s)>=2:
		M=len(s)//2
		if T==s[M]:
			pass
			print('Search target is found: ',T)
		elif T<s[M]:
			L=s[:M:]
			binary_search(L)
		else:
			R=s[M+1::]
			binary_search(R)
	else:
		print('Search Target is not found: ',T)

x=[int(num) for num in input('Enter list of numbers in powers of 2 for sorting(seperated with space): ').split()]
print()
T=int(input('enter your search element: '))
print()
merge_list=merge_sort(x)
binary_search(merge_list)

