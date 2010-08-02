#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
# Classes and function usefull for SQLite interaction
# System imports
from pysqlite2 import dbapi2 as sqlite

# Applicatives Import
import Ingredients
import Recettes

connection = sqlite.connect('soap_opera.db')
cursor = connection.cursor()

# Table Ingredient qui contient toutes les donnees generiques
cursor.execute('CREATE TABLE "Ingredients" (ref VARCHAR(50) PRIMARY KEY, famille VARCHAR(50), nom VARCHAR(50))')
connection.commit()

# Table AcideGras qui contient les compositions en Acide Gras, la SAP et l'INS des gras utilisés.
# Lien avec la table Ingredients par la reference.
cursor.execute('CREATE TABLE "AcideGras" (ref VARCHAR(50) PRIMARY KEY, ins NUMBER, sap NUMBER, lauric NUMBER)')
connection.commit()

# Table de saturation deux champs, nom (unique) et boolean saturation
cursor.execute('CREATE TABLE "Saturation" (nom VARCHAR(50) PRIMARY KEY, saturation BOOLEAN)')
connection.commit()

# Feed in some dummy datas
cursor.execute('INSERT INTO "Ingredients" VALUES ("1", "Gras", "UnGras")')
cursor.execute('INSERT INTO "AcideGras" VALUES ("1", 123, 287, 44)')
cursor.execute('INSERT INTO "Saturation" VALUES ("lauric", true)')
connection.commit()

