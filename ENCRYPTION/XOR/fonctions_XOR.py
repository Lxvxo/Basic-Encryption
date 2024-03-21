# coding: utf-8
"""
Auteur : Zodiac
Date : 26/11/2022
Objectif générale: Chiffrer ou Déchiffrer un message avec un chiffrement XOR
Objectif du fichier : Stocker les fonctions nécessaire au chiffrement XOR
"""
# BEGINNING

# modules nécessaires
from hashlib import sha256

# Fonctions

def XOR_file(key : str, name_file : str) -> None:
    """Chiffre un fichier avec un chiffrement XOR

    Args:
        key (str): clé de sécurité
        name_file (str): chemin relatif ou chemin absolu du fichier

    Returns:
        None
    """
    key : bytes = sha256(key.encode('utf-8')).digest() # fonction de hashage et affichage en bytes
    list_bytes : list[bytes]= []
    with open(name_file, "rb") as file_read : # lecture du fichier en bytes
        i : int = 0 # compteur, utile dans le cas ou la clé n'a pas la même taille que le fichier
        while file_read.peek():  # quand le fichier est lu totalement, return false
            c : int = ord(file_read.read(1)) # lecture d'un octet
            j : int = i % 256 # indice de la clé 
            list_bytes.append(bytes([c^key[j]])) # effectue l'opération XOR et ajoute à la liste le byte
    with open(name_file, "wb") as file_write : # écriture du fichier en bytes
        for byte in list_bytes:
            file_write.write(byte)

#END