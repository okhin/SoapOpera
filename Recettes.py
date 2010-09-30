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

	def getChild(this):
		"""on renvoie les ID de tous les enfants de ce node"""
		db.cursor.execute("SELECT id FROM Recette WHERE parent LIKE '?';", this.nom)
		return db.cursor.fetchall()
		
	def save(this):
		"""On efface le contenu de la precedente version pour y stocker celui de la nouvelle"""
		# Pour la table recette on fait d'abord un UPDATE
		db.cursor.execute("INSERT OR REPLACE INTO Recette VALUES (ref = ?, version = ?, parent = ?, surgraissage = ?, concentration = ?);", this.nom, this.version, this.parent, this.surgraissage, this.concentration)
		db.connection.commit()

		# On recupère l'id de cette recette (même ref)
		db.cursor.execute("SELECT id FROM Recette WHERE ref = ?;", this.nom)
		rkey = db.cursor.fetchone;

		# On sauvegarde les gras maintenant
		for (taux, gras) in this.listeGras:
			# On commence par recuperer l'ID de l'acidegras
			db.cursor.execute("DELETE FROM rec_acidegras WHERE rec_id = ?;", rkey[0])
			db.cursor.execute("SELECT a.id FROM AcideGras as a, Ingredients as i WHERE a.id = i.id AND i.nom = ?;", gras)
			gkey = db.cursor.fetchone()

			# On insere ensuite le tout dans la relation recette/AcideGras
			db.cursor.execute("INSERT INTO rec_acidegras VALUES (?, ?, ?);", rkey[0], gkey[0], taux)
			db.connection.commit()

		for (taux, he) in this.he:
			# Meme chose pour les he, sauf que l'id est plus simple a recuperer
			db.cursor.execute("DELETE FROM rec_he WHERE rec_id = ?;", rkey[0])
			db.cursor.execute("SELECT id FROM Ingredients WHERE famille = 'HE'AND nom = ?;", he)
			hkey = db.cursor.fetchone()

			db.cursor.execute("INSERT INTO rec_he VALUES(?, ?, ?);", rkey[0], hkey[0], taux)
			db.connection.commit()

		for (taux, add) in this.additifs:
			# Et encore une fois pour les additif
			db.cursor.execute("DELETE FROM rec_additifs WHERE rec_id = ?;", rkey[0])
			db.cursos.execute("SELECT id FROM Ingredients WHERE nom = ?;", add)
			akey = db.cursor.fetchone()

			db.cursor.execute("INSERT INTO rec_additifs VALUES(?, ?, ?);", rkey[0], akey[0], taux)
			db.connection.commit()
