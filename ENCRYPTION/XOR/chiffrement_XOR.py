# coding : utf-8
"""
Auteur : Zodiac
Date : 24/11/2022
Objectif générale: Chiffrer ou Déchiffrer un message avec un chiffrement XOR
Objectif : Lancer un programme permettant le chiffrement ou déchiffrement XOR d'un fichier.txt 
"""
# BEGINNING

#Fonctions nécessaires
from fonctions_XOR import XOR_file

"""
Chiffre ou Déchiffre un fichier texte avec la méthode XOR
"""
name_file: str = input("Entrez le chemin du fichier relatif ou absolu du fichier : \n")

key: str = input("Entrez la clé de sécurité : \n")

XOR_file(key, name_file)

print("Sucess")

#END