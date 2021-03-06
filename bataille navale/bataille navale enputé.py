from turtle import *

def plouf(col, lign, coul):
	x = -160+ (ord(col)-97)*40
	y = 160 + (ord(lign) - 49)*40
	color(coul)
	up()
	goto(x,y)
	begin_fill()
	down()
	for line in range (4):
		forward(40)
		right(90)
	end_fill()
	
def dessinquadrillage():
	color("#A034C0", "#A004C0")
	for ligne in range (8+1):
	   up()
	   goto(-4*40,4*40-40*ligne)
	   down()
	   forward(40*8)
	left(90)
	for col in range (8+1):
 	   up()
 	   goto(-4*40+40*col,4*40)
 	   down()
 	   backward(40*8)
	right(90)
	
	

	