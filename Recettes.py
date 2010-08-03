#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

class Recette:
	"""Une classe pour stocker les recettes"""
	surgraissage = 0.08
	soude = 0
	concentration = 0.35
	def __init__(self, acideGras, he, additifs):
		"""Les arguments sont des listes de tuples avec ratio/ingredients"""
		this.listeGras = [(pourcent, gras) for (x,v) in acideGras if v.isinstance(Ingredients.Gras)]
		this.he = he
		this.additifs = additifs

	def soude(self):
		"""Quantité de soude en pourcentage.
		On travaille en NaOH donc le ratio est de 40/56,1
		comme la sap est en soude par kilo, on divise par 1000"""
		this.soude = [ pourcent * gras.sap * 40/56100 for (pourcent, gras) in this.listeGras ].sum()

	def eau(self):
		"""Concentration = eau/graisse
		eau = concentration*graisse"""
		this.eau = this.concentration * this.masse

	def satUnsat(self):
		# On commence par rafraîchir les gras de la recette
		this.sat = this.unsat = 0
		for (taux, gras) in this.listeGras:
			this.sat += this.gras.acideGras.saturation() * taux
			this.unsat += this.gras.acideGras.unsaturation() * taux
