from turtle import *
def draw(n,s=2,l=10):
	j="00"
	pu()
	goto(0,0)
	pd()
	seth(0)
	pensize(s)
	for i in n:
		if len(j)==2:
			j=i
		else:
			j+=i
			lt(int(j[0])*l)
			fd(int(j[1])*l)
			if isdown():
				pu()
			else:
				pd()
	pu()
	goto(999,999)