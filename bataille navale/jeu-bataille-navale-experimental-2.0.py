# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 23:06:48 2019

Jeu Bataille Navale
"""

import sys # Permet d'utiliser "sys.exit()" pour arrêter le programme en milieu de code


from random import randint, choice

ordi = []
colonnes = ("a", "b", "c", "d", "e", "f", "g", "h")
lignes = ("1", "2", "3", "4", "5", "6", "7", "8")
colonnes_petit2 = ("a", "b", "c", "d", "e", "f", "g")
colonnes_petit3 = ("a", "b", "c", "d", "e", "f")
colonnes_petit4 = ("a", "b", "c", "d", "e")
colonnes_petit5 = ("a", "b", "c", "d")
jouer = True
erreur_jouer = True # Pour rentrer dans la boucle permettant de demander si le joueur veut rejouer

colonne = []
ligne = []
nb_total_de_cases_rouge = 4 + 3 + 2
cases_deja_touchees = [[], []]

from turtle import reset, setup, speed, hideturtle, color, up, goto, down, forward, left, right, begin_fill, end_fill, write

reset() # Initialise la fenêtre turtle (pour chaque démarrage)
setup(405, 405, 50, 50) # Dimensions et positioneement de la fenêtre
speed(10) # Vitesse de la tortue (dessine vite)
hideturtle() # Cache la tortue


# Valeurs par défaut
def initialisation():
	nb_total_de_cases_rouge = 4 + 3 + 2
	nettoyer()
	ordi = bateaux() # Nouveau bateau
	jouer = True # Continuer la boucle principale
	erreur = False
	return nb_total_de_cases_rouge, ordi, jouer, erreur


# Création des bateaux
def bateaux():
	# Bateau à 4 cases (premier index des coordonnées : 0)
	hasard = randint(1, 2)

	if hasard == 1:
		colonne.append(choice(colonnes_petit4))
		ligne.append(randint(1, 8))

		for i in range(1, 4): # Valeurs de "i" : 1, 2, 3.
			colonne.append(chr(ord(colonne[0]) + i)) # Utilisation de la table ASCII
			ligne.append(ligne[0]) # Même ligne pour former un navire droit

	else:
		colonne.append(choice(colonnes))
		ligne.append(randint(1, 5))

		for i in range(1, 4): # Valeurs de "i" : 1, 2, 3.
			colonne.append(colonne[0]) # Même colonne pour former un navire droit
			ligne.append(ligne[0] + i)


	# Bateau à 3 cases (premier index des coordonnées : 4)
	hasard = randint(1, 2)
	pas_trouve = True

	while pas_trouve:
		pas_trouve = False

		if hasard == 1:
			colonne.append(choice(colonnes_petit3))
			ligne.append(randint(1, 8))

			for i in range(1, 3): # Valeurs de "i" : 1, 2.
				colonne.append(chr(ord(colonne[4]) + i)) # Utilisation de la table ASCII
				ligne.append(ligne[4]) # Même ligne pour former un navire droit

		else:
			colonne.append(choice(colonnes))
			ligne.append(randint(1, 6))

			for i in range(1, 3): # Valeurs de "i" : 1, 2.
				colonne.append(colonne[4]) # Même colonne pour former un navire droit
				ligne.append(ligne[4] + i)


		# Vérifivation que les coordonnées choisies ne soient pas déjà prises
		for index_bateau3 in range(4, 7):
			for index_bateau4 in range(0, 4):
				if colonne[index_bateau3] == colonne[index_bateau4]: # Si deux x est déjà pris, peut-être pas y ?
					if ligne[index_bateau3] == ligne [index_bateau4]: # Si y aussi, faut tout recommencer...
						# Suppression de toutes les valeurs entre 4 et 7 (celle du bateau à 3 cases)
						for i in range(4, 7):
							del colonne[i]
							del ligne[i]
							pas_trouve = True # C'est reparti pour un tour...

						index_bateau3 = index_bateau4 = 100 # Sortons de ces 2 boucles pour revenir à la principale !


	# Bateau à 2 cases (premier index des coordonnées : 7)
	hasard = randint(1, 2)
	pas_trouve = True

	while pas_trouve:
		pas_trouve = False

		if hasard == 1:
			colonne.append(choice(colonnes_petit3))
			ligne.append(randint(1, 8))
			colonne.append(chr(ord(colonne[7]) + 1)) # Utilisation de la table ASCII
			ligne.append(ligne[7])

		else:
			colonne.append(choice(colonnes))
			ligne.append(randint(1, 6))
			colonne.append(colonne[7])
			ligne.append(ligne[7] + 1)


		# Vérifivation que les coordonnées choisies ne soient pas déjà prises
		for index_bateau2 in range(7, 9):
			for index_bateau34 in range(0, 7):
				if colonne[index_bateau2] == colonne[index_bateau34]: # Si deux x est déjà pris, peut-être pas y ?
					if ligne[index_bateau2] == ligne [index_bateau34]: # Si y aussi, faut tout recommencer...
						# Suppression de toutes les valeurs entre 4 et 7 (celle du bateau à 3 cases)
						for i in range(7, 9):
							del colonne[i]
							del ligne[i]
							pas_trouve = True # C'est reparti pour un tour...

						index_bateau3 = index_bateau4 = 100 # Sortons de ces 2 boucles pour revenir à la principale !

	return colonne, ligne


# Vérification de la saisie du joueur
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


# Réponse de la saisie du joueur (plouf ou touché ?)
def traitement(joueur, ordi, nb_total_de_cases_rouge, jouer, cases_deja_touchees):
	start = start_touchee = 0 # Où démarrer la recherche d'index dans la liste ?
	couleur = "blue"
	case_touchee = False

	if joueur[0] in ordi[0]: # Si la colonne correspond à une de la liste

		# Tant que :
		#	1. On a pas vérifié la totalité des possibilités (start <= 8)
		#	2. La partie n'est pas terminé (jouer == True)
		#	3. Aucune case n'a été touchée (case_touchee == False)
		while start <= 8 and jouer and case_touchee == False:

			try:
				position = ordi[0].index(joueur[0], start) # Où se situe-t-elle ?

				if joueur[1] == ordi[1][position]: # Dans ce cas, il y a bien un bateau !

					while start_touchee <= 8 and couleur == "blue":

						if joueur[0] in cases_deja_touchees[0]:
							try:
								position_touchee = cases_deja_touchees[0].index(joueur[0], start_touchee) # Où se situe-t-elle ?

								if joueur[1] == cases_deja_touchees[1][position_touchee]:
									couleur = "red" # Pour éviter qu'elle soit recouvert de bleu alors qu'elle était rouge

								start_touchee = position_touchee + 1

							except ValueError: # Cette case n'a donc jamais été touchées
								cases_deja_touchees, joueur, case_touchee, couleur, nb_total_de_cases_rouge, jouer = touchee(cases_deja_touchees, joueur, case_touchee, couleur, nb_total_de_cases_rouge, jouer)

						else:
							cases_deja_touchees, joueur, case_touchee, couleur, nb_total_de_cases_rouge, jouer = touchee(cases_deja_touchees, joueur, case_touchee, couleur, nb_total_de_cases_rouge, jouer)

				start = position + 1

			except ValueError: # Erreur produite si "jouer[0]" n'est pas trouvé dans "ordi[0]"
				start = 10 # Pour sorir de la boucle


	if case_touchee:
		print("Touché !")

	elif couleur == "red":
		print("Déjà touché !")

	else:
		print("Plouf !")

	#print(cases_deja_touchees)
	#print("Nb de cases à toucher :", nb_total_de_cases_rouge)

	return couleur, nb_total_de_cases_rouge, jouer, cases_deja_touchees


# Lorsqu'une nouvelle case est touchée
def touchee(cases_deja_touchees, joueur, case_touchee, couleur, nb_total_de_cases_rouge, jouer):
	cases_deja_touchees[0].append(joueur[0]) # Pour se rappeler que cette case n'est plus bonne !
	cases_deja_touchees[1].append(joueur[1]) # Pour se rappeler que cette case n'est plus bonne !
	case_touchee = True # Pour sorit de la boucle
	couleur = "red"
	nb_total_de_cases_rouge -= 1

	if nb_total_de_cases_rouge == 0:
		jouer = False

	return cases_deja_touchees, joueur, case_touchee, couleur, nb_total_de_cases_rouge, jouer


# Création de l'aire de jeu (quadrillage violet)
def dessin_quadrillage():
	global colonnes
	""" Aire de jeu en 8 * 8 dans une fenêtre turtle """
	color("#A034C0", "#A004C0")

	# Pour tracer les lignes
	for ligne in range(8 + 1):
		up() # Lève le crayon
		goto(-4 * 40, 4 * 40 - 40 * ligne) # Déplace (x, y) en haut gauche
		down() # Baisse le crayon
		forward(40 * 8) # Trace la distance forward

		if ligne < 8:
			up()
			goto(-170, 130 - 40 * ligne)
			down()
			write(ligne + 1)


	# Pour tracer les colonnes
	right(90)
	for colonne in range(8 + 1):
		up()
		goto(-4 * 40 + 40 * colonne, 4 * 40)
		down()
		forward(40 * 8)

		if colonne < 8:
			up()
			goto(-140 + 40 * colonne, 160)
			down()
			write(colonnes[colonne])

	left(90)


# Coloration aux coordonées colonne/ligne saisies à la couleur souhaitée
def plouf(col, lign, coul):
	""" Dessine le tir aux coordonées colonne/ligne à la couleur souhaitée :
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


# Vérification que la partie est terminée ou pas
def rejouer(jouer, erreur):
	global ordi
	if jouer == False:
		print("Coulé !")
		while erreur:
			reponse = input("Nouvelle partie ? (oui/non) : ")

			if reponse == "oui":
				nb_total_de_cases_rouge, ordi, jouer, erreur = initialisation()

			elif reponse == "non":
				erreur = False

			else:
				erreur = True

	return jouer


# Coloration de tout le quadrillage en blanc pour créer une nouvelle aire de jeu
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

ordi = bateaux()
#print(ordi) # En développant...
dessin_quadrillage()

while jouer:
	joueur = saisie(colonnes, lignes)
	couleur, nb_total_de_cases_rouge, jouer, cases_deja_touchees = traitement(joueur, ordi, nb_total_de_cases_rouge, jouer, cases_deja_touchees)
	plouf(joueur[0], joueur[1], couleur)
	jouer = rejouer(jouer, erreur_jouer)
