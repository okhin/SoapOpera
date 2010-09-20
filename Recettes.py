#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import Ingredients
import Databases as db

class Recette:
	"""Une classe pour stocker les recettes"""
	surgraissage = 0.08
	soude = 0
	concentration = 0.38
	nom = "REC"
	version = 0
	parent = ""

	def __init__(this):
		"""Les arguments sont des listes de tuples avec ratio/ingredients"""
		this.listeGras = list()
		this.he = list()
		this.additifs = list()

	def soude(this):
		"""Quantité de soude en pourcentage.
		On travaille en NaOH donc le ratio est de 40/56,1
		comme la sap est en soude par kilo, on divise par 1000"""
		soude = 0.0
		for (taux, gras) in this.listeGras:
			acidegras = Ingredients.Gras()
			acidegras.load(gras)
			soude += float(taux) * float(acidegras.sap) * ( 40.0 / 56100.0) * (1.0 - this.surgraissage)
		return soude

	def satUnsat(this):
		# On commence par rafraîchir les gras de la recette
		this.sat =  0.0
		this.unsat = 0.0
		for (taux, nom) in this.listeGras:
			gras = Ingredients.Gras()
			gras.load(nom)
			this.sat += gras.saturation() * taux
			this.unsat += gras.unsaturation() * taux

	def isChildOf(this, parent):
		"""Est-ce que cette recette descend d'une autre"""
		if parent.nom == this.parent and this.parent != "":
			return true
		return false

	def isSiblingOf(this, child):
		"""Est-ce que cette recette a un parent commun avec une autre"""
		if child.parent == this.parent and this.parent != "":
			return true
		return false

	def save(this):
		db.cursor.execute("SELECT * FROM Recette WHERE ref LIKE 'nom';")
		exist = db.cursor.fetchone()
		if exist != None:
			# On a donc déjà des versions de cette recette dans la base
			this.version = db.cursor.execute("SELECT max(version) FROM Recette WHERE ref LIKE 'nom';") + 1
		db.cursor.execute("INSERT INTO Recette VALUES (ref = ?, version = ?, parent = ?, surgraissage = ?, concentration = ?);", this.nom, this.version, this.parent, this.surgraissage, this.concentration)
		db.connection.commit()

		# On recupère l'id de cette recette (même ref + même version)
		db.cursor.execute("SELECT id FROM Recette WHERE version = ? AND ref = ?;", this.version, this.nom)
		rkey = db.cursor.fetchone;

		# On sauvegarde les gras maintenant
		for (taux, gras) in this.listeGras:
			# On commence par recuperer l'ID de l'acidegras
			db.cursor.execute("SELECT a.id FROM AcideGras as a, Ingredients as i WHERE a.id = i.id AND i.nom = ?;", gras)
			gkey = db.cursor.fetchone()

			# On insere ensuite le tout dans la relation recette/AcideGras
			db.cursor.execute("INSERT INTO rec_acidegras VALUES (?, ?, ?);", rkey[0], gkey[0], taux)
			db.connection.commit()

		for (taux, he) in this.he:
			# Meme chose pour les he, sauf que l'id est plus simple a recuperer
			db.cursor.execute("SELECT id FROM Ingredients WHERE famille = 'HE'AND nom = ?;", he)
			hkey = db.cursor.fetchone()

			db.cursor.execute("INSERT INTO rec_he VALUES(?, ?, ?);", rkey[0], hkey[0], taux)
			db.connection.commit()

		for (taux, add) in this.additifs:
			# Et encore u ne fois pour les additif
			db.cursos.execute("SELECT id FROM Ingredients WHERE nom = ?;", add)
			akey = db.cursor.fetchone()

			db.cursor.execute("INSERT INTO rec_additifs VALUES(?, ?, ?);", rkey[0], akey[0], taux)
			db.connectoion.commit()
