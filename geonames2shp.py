# -*- coding: utf-8 -*-

class Application(object):

	def __init__(self):
		"""Constructeur de la fenêtre principale"""
		self.root = Tk()
		self.root.title('import de fichier geonames')
		entree = Entry(self.root)

	def check_file(name):
		"""Récupération du fichier à traiter"""
		from os import chdir, getcwd
		chdir(getcwd())





if __name__ == '__main__':
	from Tkinter import *
	from math import log10