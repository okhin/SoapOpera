#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
# Classes de definition d'un Ingrédient

class Ingredient():
	"""La classe de base pour les ingredients, ajouts et autres trucs divers"""
	def __init__(this, nom, ref, famille):
		this.ref = ref
		this.famille = famille
		this.nom = nom

	def nom(this):
		"""Si le nom lation a une longueur nulle, c'est qu'il n'est pas défini, donc on retourne le nom vulgaire"""
		return this.latin if len(this.latin) > 0 else this.nom

	def __eq__(this, other):
		"""Un comparateur d'ingredients, pour vérifier si deux composants sont les mêmes. On vérifie les references des objets"""
		return this.ref() == other.ref()

class AcidesGras(dict):
	"""Les indices (trucs en latins bizarre) qui définissent la saturation des gras.
	c'est un dictionnaire de tuples. La clef est le nom de l'indice et le tuple
	est un tuple de valeur définissant le type (sat/unsat) et le pourcentage dans le gras. 

	On a donc {acide:(saturation,ratio)}"""
	def saturation(this):
		sat = 0
		for (saturation, ratio) in this.items():
			if saturation:
				sat += ratio
		return sat

	def unsaturation(this):
		return 100 - this.saturation()

class Gras(Ingredient):
	"""La gestion des graisses pour faire le savon"""
	acidesGras = AcidesGras({})
	def __init__(this, nom, ref, sap = 0, ins = 0):
		Ingredient.__init__(this, nom, ref, 'Gras')
		this.sap = sap
		this.ins = ins

	def getAcideGras(this, acide):
		"""On récupère un acide gras particulier.""" 
		return this.acidesGras[acide]
