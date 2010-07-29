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
		"""Si le nom lation a une longueur nulle, c'est qu'il n'est pas défini, donc on retourne le nom vulgaire"""
		return this.latin if len(this.latin) > 0 else this.nom
	def operator.__eq__(this, other):
		"""Un comparateur d'ingredients, pour vérifier si deux composants sont les mêmes. On vérifie les references des objets"""
		return this.ref() == other.ref()

class Gras(Ingredient):
	"""La gestion des graisses pour faire le savon"""
	acidesGras = new AcideGras()
	def __init__(this, nom, ref, "Gras", sap = 0, ins = 0):
		Ingredient.__init__(this, nom, stock)
		this.sap = sap
		this.ins = ins

	def soude(this):
		"""Calcul la quantite de soude par gramme de gras
		La sap est à multiplier par 0,713 pour avoir la quantite de soude par kilo de gras"""
		return this.sap * 0.713/1000

	def getAcideGras(this, acide):
		"""On récupère un acide gras particulier.""" 
		return this.acidesGras[acide]

class AcidesGras(Dict):
	"""Les indices (trucs en latins bizarre) qui définissent la saturation des gras.
	c'ets un dictionnaire de tuples. La clef est le nom de l'indice et le tuple
	est un tuple de valeur définissant le type (sat/unsat) et le pourcentage dans le gras. 

	On a donc {acide:(saturation,ratio)}"""

	def saturation(this):
		sat = 0
		for (saturation, ratio) in this.items():
			if saturation:
				sat += ratio
		return sat
