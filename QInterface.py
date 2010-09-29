#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import Recettes
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from gtk import icon_theme_get_default


class MainWindow(QtGui.QMainWindow):
	"""La fenêtre principale de l'application."""
	def __init__(self):
		QtGui.QMainWindow.__init__(self)

		# Taille par défaut, voir a agrandir ça plus tard
		self.setGeometry(300, 300, 250, 150)
		self.setWindowTitle('Soap Opera')

		# Les actions, c'est là qu'on met l'intelligence de l'iface
		# rOpen: ouverture d'une recette
		iconTheme = icon_theme_get_default()
		icon = iconTheme.lookup_icon("document-open", 32, 0)
		rOpen = QtGui.QAction(QtGui.QIcon(icon.get_filename()), 'Ouvrir', self)
		rOpen.setShortcut('Ctrl+R')
		rOpen.setStatusTip('Ouvre une Recette deja existante en base.')
		rOpen.triggered.connect(self.recipe_open)

		# La barre de statut, qui servira a afficher des trucs
		status = self.statusBar()
		status.showMessage('Ready')

		# La barre de menu, parceque nous le valons bien
		menu = self.menuBar()
		fichier = menu.addMenu('&Fichier')
		recette = menu.addMenu('&Recette')
		recette.addAction(rOpen)
		ingredients = menu.addMenu('&Ingredients')
		outils = menu.addMenu('&Outils')

		# La toolbar pour les principales actions
		tool = self.addToolBar('Tools')
		tool.addAction(rOpen)

		# Test de QTREE Widget, on le deplacera plus tard
		tree = QtGui.QTreeView(self)
	def recipe_open(self):
	"""On va utiliser QTreeViewWidget ici, et ça va piquer ma tête"""	

# Appel de l'application
app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())
