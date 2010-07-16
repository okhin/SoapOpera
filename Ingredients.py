#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
# Classe de definition d'un Ingrédient
class Ingredient:
	"""A base class for defining products and ingredients used in recipes"""
	def __init__(this, ref, stock = 0):
		this.ref = ref
		this.stock = stock
	def setNom(this, nom):
		this.nom = nom
	def operator.__eq__(self, other):
		return this.ref == other.ref

class Gras(Ingredient):
	"""A class that defines the Oil used in recipes"""
	def __init__(this, nom, stock = 0, sap = 0, ins = 0):
		Ingredient.__init__(this, nom, stock)
		this.sap = sap
		this.ins = ins
	def soude(this):
		return this.sap * 0.713/1000

class HE(Ingredient):
	"""A class for Esential oils"""
	def dose(this, pcent = 1, volume):
		"""We can choose the HE dosage in soap"""
		if (pcent > 100 ):
			pcent = 100
		return volume * (pcent/100) / 250

class Additif(Ingredient):
	"""A class for all the things we had in the soap. We can choose a concentration (grammes of additif per liter of soap)"""
	def __init__(this, nom, stock = 0, concentration = 0):
		Ingredient.__init__(this, nom, stock)
		this.concentration = concentration
	def dose(this, volume):
		return volume * (concentration/1000) #We have concentration as g/l but volume is ml)
