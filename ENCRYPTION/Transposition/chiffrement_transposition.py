# coding: utf-8
"""
Auteur : Zodiac
Date : 25/11/2022
Objectif générale : Chiffrer ou Déchiffrer un message en code Transposition
Objectif du fichier : Lancer un programme permettant le chiffrement ou déchiffrement d'un fichier.txt par Transposition
"""

# Fonctions nécessaires
from fonctions_transposition import transposition_file, transform_key_str

##BEGINNING
"""
Chiffre ou Déchiffre un fichier texte avec la méthode Transposition
"""
name_file: str = input("Entrez le chemin du fichier relatif ou absolu du fichier : \n")

key_str : str = (input("Entrez la clé de sécurité sous la forme X,X,X,X,X,X,X ... : \n"))

transposition_file(transform_key_str(key_str), name_file)

print("Success")

# END