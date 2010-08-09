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

	def calcSoude(this):
		"""Quantité de soude en pourcentage.
		On travaille en NaOH donc le ratio est de 40/56,1
		comme la sap est en soude par kilo, on divise par 1000"""
		this.soude = 0
		for (taux, gras) in this.listeGras:
			acidegras = Ingredients.Gras()
			acidegras.load(gras)
			this.soude += float(taux) * float(acidegras.sap) * ( 40 / 56100)

	def calcEau(this):
		"""Concentration = eau/graisse
		eau = concentration*graisse"""
		this.eau = this.concentration * this.masse

	def satUnsat(this):
		# On commence par rafraîchir les gras de la recette
		this.sat = this.unsat = 0
		for (taux, gras) in this.listeGras:
			acidegras = Ingredients.Gras()
			acidegras.load(gras)
			this.sat += acidegras.acideGras.saturation() * taux
			this.unsat += acidegras.acideGras.unsaturation() * taux
