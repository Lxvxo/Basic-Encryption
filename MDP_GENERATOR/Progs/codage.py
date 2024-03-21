# -*- coding: utf-8 -*-
"""
Auteur :Livio SS
Objectif : Crypter un message en code César
Date: 15/11/2022
Type : Programme
"""

from codage_fonction import *

nom_fichier = input("Entrer le nom du fichier à créer : \n")
message = input("Entrez votre message : \n")
clé = int(input("Entrez la clé de sécurité : \n"))



codage(nom_fichier+".txt",message, clé)
