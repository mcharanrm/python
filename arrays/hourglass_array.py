#ProblemStatement:
#https://www.hackerrank.com/challenges/2d-array/problem

'''
after complete sweep of 1 3 columns, need to set \
m_row=0;m_col=0 but row+=1 and col+=1
m_row,m_col remains same, we change row,col after one complete sweep.
'''
	
def hourglass_array():
	array=list()
	for num in range(6):
		array.append(list(map(int,input('enter numbers: ').strip().split())))
	row=0;col=3;hg=0;counter=0
	m_row=0;m_col=3
	tmp_array=list()
	while True:
		if m_col<=len(array):
			for i in range(m_row,m_col):
				for j in range(row,col):	#make sure row and col values are updated properly at end of loop
					if counter==0 or counter==2:
						hg+=array[i][j]
					elif counter==1 and j==row+1:
						hg+=array[i][j]		#need to reset hourglass values after appending to list	
				if counter<2:
					counter+=1
				else:
					tmp_array.append(hg);hg=0;counter=0
					m_row+=1;m_col+=1
		elif m_col>len(array) and col<len(array[0]):
			row+=1;col+=1
			m_row=0;m_col=3
		else:
			tmp_array.sort(reverse=True)
			print(tmp_array[0])
			break


if globals()['__name__']=='__main__':
	hourglass_array()
			
