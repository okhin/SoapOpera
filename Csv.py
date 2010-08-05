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

def load(filename, key, value):
	"""On charge un élément depuis un fichier particulier en cherchant une valeur dans une clef
	On retourne un dictionnaire de résultat ou une liste vide (None)."""
	reader = csv.DictReader(open(filename, 'rb'))
	try:
		return [row for row in reader if row[key] == value]
	except csv.Error, e:
		sys.exit("file %s, line %d: %s" % (filename, csvReader.line_num, e))
	# If not found, return none	
	return None

def loadall(filename):
	"""On charge toutes les lignes d'un CSV dans une liste de tuples"""
	retour = []
	reader = csv.DictReader(open(filename, 'rb'))
	for row in reader:
		retour.append(row)
	return retour
