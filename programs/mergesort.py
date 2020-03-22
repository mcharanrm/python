# Mergesort

'''Assumptions:
1.Using Recursion Concept
2.Trying for powers of 2 [easy to understand recusrive calls]'''

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


if globals()['__name__']=='__main__':
	x=[int(num) for num in input('Enter list of numbers sorting(seperated with space): ').split()]
	merge_list=merge_sort(x)
	print(merge_list)
