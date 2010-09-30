#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# System modules import
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from gtk import icon_theme_get_default

# User modules import
import Recettes
import Databases as db

class MainWindow(QtGui.QMainWindow):
	"""La fenêtre principale de l'application."""
	def __init__(self):
		QtGui.QMainWindow.__init__(self)

		# Taille par défaut, voir a agrandir ça plus tard
		self.setGeometry(300, 300, 250, 150)
		self.setWindowTitle('Soap Opera')

		# Les actions, c'est là qu'on met l'intelligence de l'iface
		# On commence par gerer les icones en fait
		iconTheme = icon_theme_get_default()
		iconOpen = iconTheme.lookup_icon("document-open", 32, 0)

		# rOpen: ouverture d'une recette
		rOpen = QtGui.QAction(QtGui.QIcon(iconOpen.get_filename()), 'Ouvrir', self)
		rOpen.setShortcut('Ctrl+R')
		rOpen.setStatusTip('Ouvre une Recette deja existante en base.')
		rOpen.triggered.connect(self.recipe_open)

		# iImport: import des ingredients depuis un csv
		iImport = QtGui.QAction('Importer les ingredients', self)
		iImport.setShortcut('Ctrl+I')
		iImport.setStatusTip('Importe la liste des ingredients depuis un fichier csv')
		iImport.triggered.connect(self.ingredient_import)

		# La barre de statut, qui servira a afficher des trucs
		self.status = self.statusBar()
		self.status.showMessage('Ready')

		# La barre de menu, parceque nous le valons bien
		menu = self.menuBar()
		fichier = menu.addMenu('&Fichier')
		recette = menu.addMenu('&Recette')
		recette.addAction(rOpen)
		ingredients = menu.addMenu('&Ingredients')
		ingredients.addAction(iImport)
		outils = menu.addMenu('&Outils')

		# La toolbar pour les principales actions
		tool = self.addToolBar('Tools')
		tool.addAction(rOpen)

	def recipe_open(self):
		"""On va utiliser QTreeViewWidget ici, et ça va piquer ma tête"""	
		dialog = QtGui.QDialog()

		# On commence par faire une petite barre de bouton, ça servira toujours.
		# Open / Cancel et Horizontaux
		buttons = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Open | QtGui.QDialogButtonBox.Cancel, QtCore.Qt.Horizontal)

		# On génère ensuite un arbre qui va bien, en recuperant toutes les recettes qui n'ont
		# pas de parent et en inserant ensuite les enfants.
		tree = QtGui.QTreeWidget()
		db.cursor.execute("SELECT nom FROM Recette WHERE parent = '';")
		head = db.cursor.fetchall()
		tree.addTopLevelItems([QtGui.QTreeWidgetItem(tree, [rec]) for rec in head])

		# on les mets les uns au-dessus des autres
		vbox = QtGui.QVBoxLayout()
		vbox.addWidget(tree)
		vbox.addWidget(buttons)

		# et on centre horizontalement
		hbox = QtGui.QHBoxLayout()
		hbox.addStretch(1)
		hbox.addLayout(vbox)
		hbox.addStretch(1)

		dialog.setLayout(hbox)

		# On affiche quelque chose dans la status bar
		self.status.showMessage("Ouverture d'une recette.")

		dialog.exec_()

	def ingredient_import(self):
		"""On va utiliser un dialogue de recherche de fichier, et jouer avec la statusbar""" 
		pass

# Appel de l'application
app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())
