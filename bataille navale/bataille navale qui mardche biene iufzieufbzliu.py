from random import randint, choice
from turtle import *

ordi = ()
colonnes = ("a","b","c","d","e","f","g","h")
lignes = ("1","2","3","4","5","6","7","8")

reset()
setup(405, 405, 50, 50) 
speed(10)
hideturtle()

def plouf(col, lign, coul):
	x = -160+ (ord(col)-97)*40
	y = 160 + lign * -40 + 40
	color(coul)
	up()
	goto(x,y)
	begin_fill()
	down()
	for line in range (4):
		forward(40)
		right(90)
	end_fill()

	
def dessin_quadrillage():
	color("#A034C0", "#A004C0")
	for ligne in range(8 + 1):
		up() # Lève le crayon
		goto(-4 * 40, 4 * 40 - 40 * ligne) 
		down() # Baisse le crayon
		forward(40 * 8) 
	right(90)
	for colonne in range(8 + 1):
		up()
		goto(-4 * 40 + 40 * colonne, 4 * 40)
		down()
		forward(40 * 8)
	left(90)

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
            l = int(s[1])
            saisie = False
        else :
            print("Tu vises très mal")
   return c,l
        
        
def traitement(joueur, ordi):
    global jouer
    if joueur[0] == ordi[0] and str(joueur[1]) == str(ordi[1]):
        print("rezoin l'armée t tro forrr")
        couleur = "red"
        jouer = False
    elif joueur[0] == ordi[0] or str(joueur[1]) == str(ordi[1]):
        print("t poo loinnn, tu chauffes")
        couleur = "yellow"
        jouer = True
    else :
        print("j'espère que tu sais nager car tu te noies")
        couleur = "blue"
        jouer = True
    return couleur
	
	
ordi = bateau()
dessin_quadrillage()
jouer = True

while jouer:
    #print(ordi)
    joueur = saisie(colonnes, lignes)
    #print(joueur)
    couleur = traitement(joueur, ordi)
    plouf(joueur[0], joueur[1], couleur)
    