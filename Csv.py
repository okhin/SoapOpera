#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
# Extending objects with CSV interfaces.
# The method should be simply deduce (such as csvClass)
# This module provides some function for a lot of funnythings to
# such as parseCsvClass which load a full file.
#
# System import
import csv
import sys

# User import
import Ingredients
import Recettes

class csvHelper():
	"""Un helper générique de fichier CSV"""
	def __init__(this, filename):
		try:
			f = open(filename, 'wb')
			this.filename = filename

		except IOError, e:
			sys.exit("file %s: %s" % (filename, e))

		finally:
			close(f)

	def search(this, key, value):
		"""On cherche un élément dans une clef particulière"""
		csvReader = csv.DictReader(open(this.filename, 'rb'))
		try:
			for row in csvReader:
				if key is not in row.keys():
					raise NOKey

				if row[key] == value:
					return row

		except csv.Error, e:
			sys.exit("file %s, line %d: %s" % (this.filename, csvReader.line_num, e))
		# If not found, return none	
		return None

	def loadIngredient(this, name):
		"""On charge un ingredient depuis un dictionnaire"""
		try:
			result = this.search(name)
			ingredient = Ingredients.Ingredient(result['ref'], result['famille'], result['nom'])
			return ingredient

		except NOKey, e:
			sys.exit("file %s, name %s" % (this.filename, name, e))

	def loadGras(this, name):
		"""On charge un gras depuis un dictionnaire"""
		try:
			result = this.search(name)
			gras = Ingredients.Gras(result['ref'],
