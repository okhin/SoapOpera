#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
# Classe de definition d'un Ingrédient
class Ingredient:
	"""La classe de base pour les ingredients, ajouts et autres trucs divers"""
	def __init__(this, nom, ref, famille):
		this.ref = ref
		this.famille = famille
		this.nom = nom
	def nom(this):
		"""Si le nom lation a une longueur nulle, c'est qu'il n'est pas déini, donc on retourne le nom vulgaire"""
		return this.latin if len(this.latin) > 0 else this.nom
	def operator.__eq__(this, other):
		"""Un comparateur d'ingredients, pour vérifier si deux composants sont les mêmes. On vérifie les references des objets"""
		return this.ref() == other.ref()

class Gras(Ingredient):
	"""La gestion des graisses pour faire le savon"""
	indices = {}
	def __init__(this, nom, ref, "Gras", sap = 0, ins = 0):
		Ingredient.__init__(this, nom, stock)
		this.sap = sap
		this.ins = ins
	def soude(this):
		"""Calcul la quantite de soude par gramme de gras
		La sap est à multiplier par 0,713 pour avoir la quantite de soude par kilo de gras"""
		return this.sap * 0.713/1000
	def getIndice(this, indice):
		"""On récupère la valeur d'un indice particulier. Si il n'est pas definit, c'ets qu'il vaut 0"""
		if indice in this.indices.keys():
			return this.indices(indice)
		return 0
