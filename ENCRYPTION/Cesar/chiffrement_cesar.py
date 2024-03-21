# coding: utf-8
"""
Auteur : Zodiac
Date : 24/11/2022
Objectif générale : Chiffrer ou Déchiffrer un message en code César
Objectif du fichier : Lancer un programme permettant le chiffrement César ou déchiffrement d'un fichier.txt 
"""

# Fonctions nécessaires
from fonctions_cesar import cesar_file, transform_key

##BEGINNING
"""
Chiffre ou Déchiffre un fichier texte avec la méthode César
"""
name_file: str = input("Entrez le chemin du fichier relatif ou absolu du fichier : \n")

method: int = int(input("Entrez 1 pour chiffrer | Entrez 0 pour déchiffrer : \n"))

key: int = int(input("Entrez la clé de sécurité : \n"))

cesar_file(transform_key(key, method), name_file)

print("Success")

# END
