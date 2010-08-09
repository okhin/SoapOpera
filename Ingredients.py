#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
# Classes de definition d'un Ingrédient
# User Import
import Csv 

class Ingredient():
	"""La classe de base pour les ingredients, ajouts et autres trucs divers"""
	def nom(this):
		"""Si le nom lation a une longueur nulle, c'est qu'il n'est pas défini, donc on retourne le nom vulgaire"""
		return this.latin if len(this.latin) > 0 else this.nom

	def load(this, ref):
		loader = Csv.load("csv/ingredients.csv", "ref", ref)
		if loader is not None:
			this.ref = loader["ref"]
			this.famille = loader["famille"]
			this.nom = loader["nom"]

	def __eq__(this, other):
		"""Un comparateur d'ingredients, pour vérifier si deux composants sont les mêmes. On vérifie les references des objets"""
		return this.ref() == other.ref()

class AcidesGras(dict):
	"""Les indices (trucs en latins bizarre) qui définissent la saturation des gras.
	c'est un dictionnaire de tuples. La clef est le nom de l'indice et le tuple
	est un tuple de valeur définissant le type (sat/unsat) et le pourcentage dans le gras. 

	On a donc {acide:(nom de l'indice,valeur)}"""
	def load(this, nom):
		loader = Csv.load("csv/acidegras.csv", "nom", nom)
		this.update(loader)
		 
	def saturation(this):
		saturations = Csv.loadall("csv/saturation.csv")
		for (acide, saturation) in saturations:
			if saturation: sat += this[acide] 
		return sat

	def unsaturation(this):
		return 100 - this.saturation()

class Gras(Ingredient):
	"""La gestion des graisses pour faire le savon"""
	def load(this, ref):
		"""On récupère les données en deux temps"""
		Ingredient.load(this, ref)
		acides = AcidesGras()
		acides.load(this.ref)
		this.sap = acides.pop("sap")
		this.ins = acides.pop("ins")
		del acides["nom"]
		this.acideGras = acides
