# coding: utf-8
"""
Auteur : Zodiac
Date : 24/11/2022
Objectif générale : Chiffrer ou Déchiffrer un message en code Vignere
Objectif du fichier : Lancer un programme permettant le chiffrement ou déchiffrement Vignere d'un fichier.txt 
"""

# Fonctions nécessaires
from fonctions_vignere import vignere_file

##BEGINNING
"""
Chiffre ou Déchiffre un fichier texte avec la méthode César
"""
name_file: str = input("Entrez le chemin du fichier relatif ou absolu du fichier : \n")

signe : int = int(input("Entrez 1 pour chiffrer | Entrez -1 pour déchiffrer : \n"))

key: str = input("Entrez la clé de sécurité : \n")

vignere_file(key, name_file, signe)

print("Success")

# END

