from random import randint,choice
from turtle import *

reset()
setup(405,405,50,50)
speed(10)
hideturtle()

ordi1=()
ordi2=()
colonnes=("a","b","c","d","e","f","g","h")
lignes=("1","2","3","4","5","6","7","8")

def plouf(col,lign,coul):
    up()
    x=-160+(ord(col)-97)*40
    y=160-(ord(lign)-48)*40
    color(coul)
    goto(x,y)
    begin_fill()
    for line in range (4):
        forward(40)
        left(90)
    end_fill()
    

def dessinquadrillage():
    color("#A034C0","#A004C0")
    for ligne in range (8+1):
        up()
        goto(-4*40,4*40-40*ligne)
        down()
        forward(40*8)
    left(90)
    for col in range (8+1):
        up()
        goto(-4*40+40*col,-4*40)
        down()
        forward(40*8)
    right(90)

def bateau():
    colonne=choice(colonnes)
    ligne=choice(lignes)
    return colonne,ligne

def saisie(colonnes,lignes):
    saisie=True
    while saisie:
        s=input('Saisir une lettre entre a et h et puis un numero entre 1 et 8 (Ex: d1):')
        if s[0] in colonnes and s[1] in lignes:
            c=s[0]
            l=s[1]
            saisie=False
        else:
            print('Tir en dehors du jeu.')
    return c,l

def traitement(joueur,ordi1):
    global jouer
    touché1=False
    touché2=False
    if joueur[0]==ordi1[0] and joueur[1]==ordi1[1]:
        print('Gagné')
        if touché1==False:
            jouer=-1
            touché1=True
        return "red"
    elif joueur[0]==ordi1[0] or joueur[1]==ordi1[1]:
        print('En vue')
        return "yellow"
    else:
        print("A l'eau")
        return "blue"

    
while ordi1==ordi2:
    ordi1=bateau()
    ordi2=bateau()
jouer=2
while jouer:
    dessinquadrillage()
    print(ordi1)
    joueur=saisie(colonnes,lignes)
    print(joueur)
    coul=traitement(joueur,ordi1)
    plouf(joueur[0],joueur[1],coul)