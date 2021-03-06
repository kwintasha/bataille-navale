# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 23:06:48 2019

Jeu Bataille Navale
"""

import sys # Permet d'utiliser "sys.exit()" pour arrêter le programme en milieu de code


from random import randint, choice

ordi = ()
colonnes = ("a", "b", "c", "d", "e", "f", "g", "h")
lignes = ("1", "2", "3", "4", "5", "6", "7", "8")
jouer = True
erreur_jouer = True # Pour rentrer dans la boucle permettant de demander si le joueur veut rejouer


from turtle import reset, setup, speed, hideturtle, color, up, goto, down, forward, left, right, begin_fill, end_fill

reset() # Initialise la fenêtre turtle (pour chaque démarrage)
setup(405, 405, 50, 50) # Dimensions et positioneement de la fenêtre
speed(10) # Vitesse de la tortue (dessine vite)
hideturtle() # Cache la tortue


def bateau():
	colonne = choice(colonnes) # Choix dans la constante "colonnes"
	ligne = randint(1, 8) # Choix d'un numéro de ligne
	return colonne, ligne


def saisie(colonnes, lignes):
	saisie = True
	while saisie:
		s = input("Saisie une lettre entre A et H puis, un nombre entre 1 et 8 : ")
		s = s.lower() # Metrre tout en minuscule pour minimiser les erreurs
		
		if s == "":
			print("Erreur")

		elif s == "stop":
			sys.exit() # Arrêt total du programme

		elif s[0] in colonnes and s[1] in lignes: # Comparaison avec les tuples définies plus haut
			c = s[0]
			l = int(s[1])
			saisie = False

		else:
			print("Tir en dehors de l'air de jeu.")

	return c, l


def traitement(joueur, ordi):
	global jouer

	if joueur[0] == ordi[0] and joueur[1] == ordi[1]:
		print("Touché !")
		couleur = "red"
		jouer = False

	elif joueur[0] == ordi[0] or joueur[1] == ordi[1]:
		print("En vue !")
		couleur = "yellow"

	else:
		print("Plouf !")
		couleur = "blue"

	return couleur


def dessin_quadrillage():
	""" Aire de jeu en 8 * 8 dans une fenêtre turtle """
	color("#A034C0", "#A004C0")

	# Pour tracer les lignes
	for ligne in range(8 + 1):
		up() # Lève le crayon
		goto(-4 * 40, 4 * 40 - 40 * ligne) # Déplace (x, y) en haut gauche
		down() # Baisse le crayon
		forward(40 * 8) # Trace la distance forward

	# Pour tracer les colonnes
	right(90)
	for colonne in range(8 + 1):
		up()
		goto(-4 * 40 + 40 * colonne, 4 * 40)
		down()
		forward(40 * 8)

	left(90)


def plouf(col, lign, coul):
	""" Dessine le tir au coordonées colonne/ligne à la couleur souhaité :
		"blue" <=> A l'eau, "yellow" <=> En vue, "red" <=> Touché """
	x = -160 + (ord(col) - 97) * 40 # Reculer de 160, ajouter le nb de colonnes de 40px. En ASCII : "a" <=> 97
	y = 160 + lign * -40 + 40
	color(coul)
	up()
	goto(x, y)
	down()
	begin_fill()
	for line in range(4):
		forward(40)
		right(90)

	end_fill()


def rejouer(jouer, erreur):
	global ordi
	if jouer == False:
		while erreur:
			reponse = input("Nouvelle partie ? (oui/non) : ")

			if reponse == "oui":
				nettoyer()
				ordi = bateau() # Nouveau bateau
				jouer = True # Continuer la boucle principale
				erreur = False

			elif reponse == "non":
				erreur = False

			else:
				erreur = True

	return jouer


def nettoyer():
	color("white")
	up()
	goto(-160, 160)
	down()
	next_row = next_col = 0
	# Met en blanc toutes les lignes du quadrillage
	while next_row <= (40 * 8):
		# Met en blanc toutes les cases d'une ligne
		while next_col <= (40 * 8):
			# Met en blan une cases
			begin_fill()
			for line in range(4):
				forward(40)
				right(90)

			end_fill()
			up()
			goto(-160 + next_col, 160 - next_row)
			down()
			next_col += 40

		next_row += 40
		next_col = 0 # Il faut recommencer

	dessin_quadrillage()


# Programme principal !

ordi = bateau()
dessin_quadrillage()

while jouer:
	joueur = saisie(colonnes, lignes)
	couleur = traitement(joueur, ordi)
	plouf(joueur[0], joueur[1], couleur)
	jouer = rejouer(jouer, erreur_jouer)

