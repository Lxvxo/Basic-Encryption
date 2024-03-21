# -*- coding: utf-8 -*-
"""
Auteur :Livio SS
Objectif : Décrypter un message en code César
Date: 15/11/2022
Type : Programme
"""

from codage_fonction import *


nom_fichier = input("Entrer le nom du fichier existant : \n")
clé = int(input("Entrez la clé de sécurité : \n"))

decodage(nom_fichier+".txt",clé)

