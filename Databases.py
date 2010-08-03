#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
# Classes and function usefull for SQLite interaction
# System imports
from pysqlite2 import dbapi2 as sqlite
import os.path

# Applicatives Import
import Ingredients
import Recettes

connection = sqlite.connect('soap_opera.db')
cursor = connection.cursor()

def InitAppli():
	# Table Ingredient qui contient toutes les donnees generiques
	cursor.execute('CREATE TABLE "Ingredients" (ref VARCHAR(50) PRIMARY KEY, famille VARCHAR(50), nom VARCHAR(50))')
	connection.commit()

	# Table AcideGras qui contient les compositions en Acide Gras, la SAP et l'INS des gras utilisés.
	# Lien avec la table Ingredients par la reference.
	cursor.execute('CREATE TABLE "AcideGras" (ref VARCHAR(50) PRIMARY KEY,
		ins NUMBER, 
		sap NUMBER,
		lauric NUMBER,
		myristic NUMBER,
		palmitic NUMBER,
		stearic NUMBER,
		ricinoleic NUMBER,
		oleic NUMBER,
		linoleic NUMBER,
		linolenic NUMBER)')
	connection.commit()

	# Table de saturation deux champs, nom (unique) et boolean saturation
	cursor.execute('CREATE TABLE "Saturation" (nom VARCHAR(50) PRIMARY KEY, saturation BOOLEAN)')
	connection.commit()

	# Feed in some dummy datas
	cursor.execute('INSERT INTO "Ingredients" VALUES ("1", "Gras", "UnGras")')
	cursor.execute('INSERT INTO "AcideGras" VALUES ("1", 123, 287, 44)')
	connection.commit()

# Import Saturation from csv
def CSV_Saturation(filename):
	try:
		f = open(filename,'rb', 0)
		try:
			for lines in f.readlines():
				if line.startswith('#'):
					continue
				parts = lines.split(';')
				cursor.execute('INSERT INTO Saturation VALUES (?, ?)', (parts))
				connection.commit
		finally:
			f.close()

	except IOError:
		pass

def CSV_Ingredient(filename):
	try:
		f = open(filename, 'rb', 0)
		try:
			for line in f.readlines():
				if line.startswith('#'):
					continue
				parts = lines.split(';')
				cursor.execute('INSERT INTO Ingredients VALUES (?, ?, ?,)', (parts))
				connection.commit
		finally:
			f.close()

def CSV_AcideGras(filename):
	try:
		f = open(filename, 'rb', 0)
		try:
			for line in f.readlines():
				if line.startswith('#'):
					continue
				parts = lines.split(';')
				acideGras.add(parts[0], parts[1]) 
				cursor.execute('INSERT INTO AcideGras VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (parts))
				connection.commit
		finally:
			f.close()

def SELECT_Saturation():
	cursor.execute('SELECT * FROM Saturation')
	print cursor.fetchall()