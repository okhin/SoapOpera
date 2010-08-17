#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
# Classes and function usefull for SQLite interaction
# System imports
import sqlite3 as sqlite
import os.path

# Applicatives Import
import Csv
import Ingredients

connection = sqlite.connect('soap_opera.db')
cursor = connection.cursor()

def InitAppli():
	# Table Ingredient qui contient toutes les donnees generiques
	cursor.execute('CREATE TABLE "Ingredients" (id INTEGER PRIMARY KEY AUTOINCREMENT, ref VARCHAR(50), famille VARCHAR(50), nom VARCHAR(50))')
	connection.commit()

	# Table AcideGras qui contient les compositions en Acide Gras, la SAP et l'INS des gras utilisés.
	# Lien avec la table Ingredients par la reference.
	cursor.execute('CREATE TABLE "AcideGras" (id INTEGER PRIMARY KEY, \
		ins INTEGER, \
		sap INTEGER, \
		lauric INTEGER, \
		myristic INTEGER, \
		palmitic INTEGER, \
		stearic INTEGER, \
		ricinoleic INTEGER, \
		oleic INTEGER, \
		linoleic INTEGER, \
		linolenic INTEGER, \
		other_sat INTEGER, \
		other_unsat INTEGER)')
	connection.commit()

	# Table de saturation deux champs, nom (unique) et boolean saturation
	cursor.execute('CREATE TABLE "Saturation" (nom VARCHAR(50), saturation BOOLEAN)')
	connection.commit()

	# Tables de recette
	cursor.execute('CREATE TABLE "Recette" (id INTEGER PRIMARY KEY AUTOINCREMENT, nom VARCHAR(50), ref VARCHAR(50))')
	connection.commit()
	
	# Tables de relation recettes
	cursor.execute('CREATE TABLE "rec_acidegras" (rec_id INTEGER, acide_id, NUMBER, taux NUMBER)')
	cursor.execute('CREATE TABLE "rec_he" (rec_id INTEGER, he_id, NUMBER, taux NUMBER)')
	cursor.execute('CREATE TABLE "rec_additifs" (rec_id INTEGER, additifs_id, NUMBER, taux NUMBER)')
	connection.commit()

# Import Saturation from csv
def importSaturation(filename):
	"""Importer la saturation depuis un fichier csv."""
	cursor.execute("DELETE FROM Saturation")
	connection.commit()

	for d in Csv.loadall(filename):
		cursor.execute("INSERT INTO Saturation VALUES (?, ?)", (d["acidegras"], d["saturation"]))
		connection.commit()

def importIngredients(filename):
	"""Importer les ingredients depuis un fichier csv. Opération destructrice."""
	cursor.execute("DELETE FROM Ingredients")
	connection.commit()

	cursor.execute("INSERT INTO Ingredients VALUES (NULL, ?, ?, ?)", Csv.loadall("csv/ingredients.csv"))
	connection.commit()
