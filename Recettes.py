#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import Ingredients

class Recette:
	"""Une classe pour stocker les recettes"""
	surgraissage = 0.08
	soude = 0
	concentration = 0.35
	def __init__(this, acideGras, he, additifs):
		"""Les arguments sont des listes de tuples avec ratio/ingredients"""
		this.listeGras = acideGras
		this.he = he
		this.additifs = additifs

	def soude(this):
		"""Quantité de soude en pourcentage.
		On travaille en NaOH donc le ratio est de 40/56,1
		comme la sap est en soude par kilo, on divise par 1000"""
		soude = 0.0
		for (taux, gras) in this.listeGras:
			acidegras = Ingredients.Gras()
			acidegras.load(gras)
			soude += float(taux) * float(acidegras.sap) * ( 40.0 / 56100.0)
		return soude

	def eau(this):
		"""Concentration = eau/graisse
		eau = concentration*graisse"""
		return this.concentration 

	def satUnsat(this):
		# On commence par rafraîchir les gras de la recette
		this.sat =  0.0
		this.unsat = 0.0
		for (taux, nom) in this.listeGras:
			gras = Ingredients.Gras()
			gras.load(nom)
			print gras.acideGras
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

		nombre = len(liste)
		partial = float(taux / nombre)
		liste = [ (t - partial, i) for (t, i) in liste ]
		liste.append((taux, ingredient))

		if famille == "Gras":
			this.listeGras = liste[:]
		elif famille == "HE":
			this.he = liste[:]
		else:
			this.additifs = liste[:]
