#https://www.hackerrank.com/challenges/find-angle/problem

'''points considered: Sample Test case-1
        A					A
	'`					'`
	'  `					'    ` 
      	'    `M     find anble <MBC ?		'       `M
      10    .  `    		--> 	      10'      . ' `	
	'  .     `				'    .   '    `
	' .        ` 				' .      '       `
	'------------`				'--------'----------`
	B     10      C  			B   	 D	     C
              						 10	
Given:
sides AB and BC are length are known
Triangle ABC is right angled triangle

procedure:
1.Find length of side AC. AC=sqrt(AB**2+BC**2)
2.Find length of sides AM and MC = AC/2
3.Draw a line perpendicular to BC from M
4.Tri ABC and Tri MDC are parallel to each other. <A==<M && <B==<D && <C==<C
5.Sides are directly proportional. AB,MD && AC, MC && BC, DC
6.Calculate				and finally calculate DC by using pythogorous therom
	    AB   MD         AB*MC		
	    -- = -- --> MD= -----        	DC=sqrt(MC**2-MD**2)
	    AC   MC          AC

7.angle MBC -- tan(theta)=MD/BD and theta=atan(MD/BD)'''

from math import sqrt,atan,degrees

if __name__=='__main__':
	AB=int(input())
	BC=int(input())
	AC=sqrt((pow(AB,2)+pow(BC,2)))
	MC=AC/2
	MD=((AB*MC)/AC)
	DC=sqrt(pow(MC,2)-pow(MD,2))
	BD=BC-DC
	angle=degrees(atan(MD/BD))
	print('{:1.0f}°'.format(angle))

