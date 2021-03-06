from random import randint, choice
from turtle import *

reset()
setup(45,405,50,50)
speed(10)
hideturtle()

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
  
ordi = ()
colonnes = ("a","b","c","d","e","f","g","h")
lignes = ("1","2","3","4","5","6","7","8")

def bateau():
    colonne = choice(colonnes)
    ligne = choice(lignes)
    return colonne, ligne

def saisie(colonnes,lignes):
   saisie = True 
   while saisie:
       s = input("saisir une lettre entre a et h puis un numéro de colonne entre 1 et 8: ")
       if s[0] in colonnes and s[1] in lignes :
           c = s[0]
           l = s[1]
           saisie = False
       else :
           print("Tu vises très mal")
   return c,l
        
        
def traitement(joueur, ordi):
    global jouer
    if joueur[0] == ordi[0] and joueur[1] == ordi[1]:
        print("rejoin l'armée t tro forrr")
		return 'red'
    elif joueur[0] == ordi[0] or joueur[1] == ordi[1]:
        print("t poo loinnn, tu chauffe")
		return 'yellow'
    else :
        print("j'espère que tu sais nager car tu te noies")
		return 'blue'
        

	
	
ordi = bateau()
jouer = True
while jouer :
    print(ordi)
    joueur = saisie(colonnes,lignes)
    print(joueur)
    coul=traitement(joueur,ordi)
    jouer = False
    