#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
class Recette:
	"""Une classe pour stocker les recettes"""
	surgraissage = 0.08
	soude = 0
	concentration = 0.35
	volume = 1000
	def __init__(self, gras, he, additifs):
		"""Les arguments sont des listes de tuples avec ratio/ingredients"""
		this.gras = [(x,v) for (x,v) in gras if v.isinstance(Ingredients.Gras)]
		this.he = he
		this.additifs = additifs
	def soude(self):
		this.soude = sum([gras[0].soude()*gras[1]*self.volume for gras in self.gras])*(1 - this.surgraissage)

	def eau(self):
		"""Concentration = taux de soude pour le volume total (graisse + eau).
		Donc, graisse + eau = taux de soude / concentration
		Donc eau = taux de soude / concentration - graisse."""
		this.eau = this.soude / this.concentration - this.volume

	def satUnsat(self):
		# On commence par rafraîchir les gras de la recette
		this.sat = this.unsat = 0
		for (gras,taux) in this.gras:
			gras.saturation()
			this.sat += gras.sat * taux if gras.sat == 1
			this.unsat += gras.unsat * taux if gras.sat == 0
