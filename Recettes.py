#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import Ingredients
import Databases as db

class Recette:
	"""Une classe pour stocker les recettes"""
	surgraissage = 0.08
	soude = 0
	concentration = 0.38
	nom = "REC"

	def __init__(this):
		"""Les arguments sont des listes de tuples avec ratio/ingredients"""
		this.listeGras = list()
		this.he = list()
		this.additifs = list()

	def setNom(this):
		if this.nom != "REC":
			return
		db.cursor.execute("SELECT max(id) FROM Recettes;")
		print db.cursor.fetch()

	def soude(this):
		"""Quantité de soude en pourcentage.
		On travaille en NaOH donc le ratio est de 40/56,1
		comme la sap est en soude par kilo, on divise par 1000"""
		soude = 0.0
		for (taux, gras) in this.listeGras:
			acidegras = Ingredients.Gras()
			acidegras.load(gras)
			soude += float(taux) * float(acidegras.sap) * ( 40.0 / 56100.0) * (1.0 - this.surgraissage)
		return soude

	def satUnsat(this):
		# On commence par rafraîchir les gras de la recette
		this.sat =  0.0
		this.unsat = 0.0
		for (taux, nom) in this.listeGras:
			gras = Ingredients.Gras()
			gras.load(nom)
			this.sat += gras.saturation() * taux
			this.unsat += gras.unsaturation() * taux

	def add(this, ingredient, taux):
		ingr = Ingredients.Ingredient()
		ingr.load(ingredient)
		famille = ingr.famille
		if famille == "Gras":
			liste = this.listeGras
		elif famille == "HE":
			liste = this.he
		else:
			liste = this.additifs

		if len(liste) >= 1:
			if ingredient in [ i for (t, i) in liste ]:
				nombre = len(liste) - 1
				partial = float(taux / nombre) 
				exist = [ (t + taux, i) for (t, i) in liste if i == ingredient ]
				liste = [ (t - partial, i) for (t, i) in liste if i != ingredient and t > 0.0 ]
				liste += exist
			else:
				nombre = len(liste)
				partial = float(taux / nombre)
				liste = [ (t - partial, i) for (t, i) in liste ]
				liste.append((taux, ingredient))
		else:
			liste.append((taux, ingredient))

		if famille == "Gras":
			this.listeGras = liste[:]
		elif famille == "HE":
			this.he = liste[:]
		else:
			this.additifs = liste[:]

	def rem(this, ingredient):
		ingr = Ingredients.Ingredient()
		ingr.load(ingredient)
		famille = ingr.famille
		if famille == "Gras":
			liste = this.listeGras
		elif famille == "HE":
			liste = this.he
		else:
			liste = this.additifs

		if ingredient in [ i for (t, i) in liste ]:
			if len(liste) <= 1: liste = list()
			else:
				nombre = len(liste)
				taux = [ t for (t, i) in liste if i == ingredient ]
				partial = float(taux / nombre)
				liste = [ (t + partial, i) for (t, i) in liste if i != ingredient ]

		if famille == "Gras":
			this.listeGras = liste[:]
		elif famille == "HE":
			this.he = liste[:]
		else:
			this.additifs = liste[:]
