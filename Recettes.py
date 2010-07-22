#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
class Recette:
	"""Une classe pour stocker les recettes"""
	surgraissage = 0.08
	soude = 0
	eau = 0
	volume = 1000
	def __init__(self, gras, he, additifs):
		this.gras = [x for x in gras if isinstance(x, Ingredients.Gras)]
		this.he = he
		this.additifs = additifs
	def soude(self):
		this.soude = sum([gras[0].soude()*gras[1]*self.volume for gras in self.gras])*(1 - this.surgraissage)
