# coding: utf-8
"""
Auteur : Zodiac
Date : 25/11/2022
Objectif générale: Chiffrer ou Déchiffrer un message par Transpostion
Objectif du fichier : Stocker les fonctions nécessaire au chiffrement par transposition
"""
# BEGINNING

# module nécessaires
from random import choice
import string

# Fonctions


def permutation(bloc: str, key: list[int]) -> str:
    """Permettre les charactères d'une chaîne selon clé prédéfini

    Args:
        bloc (str): un bloc parmi le message que l'on veut chiffrer
        key (list[int]): clé pour le chiffrement

    Returns:
        str: bloc permuté
    """
    bloc_permute: list = []
    n: int = len(bloc)  # taille d'un bloc
    for i in range(n):
        indice: int = key.index(i)
        bloc_permute.append(bloc[indice])
    return "".join(bloc_permute)


def generate_key(length_key: int) -> list[int]:
    """Génère une clé de chiffrement aléatoirement

    Args:
        length_key (int): taille de la clé

    Returns:
        list[int]: clé généré
    """
    list_index: list[int] = [k for k in range(length_key)]
    key: list[int] = []
    for i in range(length_key):
        index: int = choice(list_index)
        key.append(index)
        del list_index[list_index.index(index)]
    return key


def complete(text: str, length_bloc: int, charac: str) -> str:
    """Complète un texte afin qu'il puisse être séparé en length_bloc blocs distincs

    Args:
        text (str): text à compléter
        length_bloc (int): taille d'un bloc
        charac (str): charactère pour compléter

    Returns:
        str: texte complété
    """
    difference: int = len(text) % length_bloc
    if difference == 0:
        return text
    add_length: int = length_bloc - difference
    for k in range(add_length):
        text += charac
    return text


def separate_text(text: str, length_bloc: int) -> list[str]:
    """Sépare un texte en length_bloc blocs distincts et complète le texte avec le charactère "x"

    Args:
        text (str): texte à séparer 
        length_bloc (int): taille d'un bloc

    Returns:
        list[str]: liste de tous les blocs
    """
    text: str = complete(text, length_bloc, "x")
    nb_blocs: int = len(text) // length_bloc
    list_blocs: list[str] = []
    for index_bloc in range(nb_blocs):
        bloc: str = ""
        i: int = index_bloc * length_bloc
        for index_charac in range(i, i + length_bloc):
            bloc += text[index_charac]
        list_blocs.append(bloc)
    return list_blocs


def transposition(text: str, key: list[int]) -> str:
    """Chiffre un texte avec la méthode de transposition

    Args:
        text (str): texte à chiffrer
        key (list[int]): clé pour le chiffrement

    Returns:
        str: texte chiffré
    """
    length_key: int = len(key)
    length_bloc: int = length_key
    list_blocs: list[str] = separate_text(text, length_bloc)
    text_transpose: str = ""
    for bloc in list_blocs:
        text_transpose += permutation(bloc, key)
    return text_transpose


def transposition_file(key: list[int], name_file: str) -> None:
    """Chiffre un fichier texte avec la méthode transposition

    Args:
        key (list[int]): clé pour le chiffrement
        name_file (str): chemin du fichier relatif ou absolu du fichier
    """
    result: str = ""
    with open(name_file, "r") as file_read:
        list_lines: list[str] = file_read.read().split("\n")
        for line in list_lines:
            result += transposition(line, key)
            result += "\n"
    with open(name_file, "w") as file_write:
        file_write.write(result)


def transform_key_str(key_str: str) -> list[int]:
    """Tranforme une clé sous la forme str en clé liste d'entier

    Args:
        key_str (str): clé sous la forme de str

    Returns:
        list[int]: clé sous la forme de liste d'entier
    """
    key_int: list[int] = []
    for charc in key_str:
        if charc in string.digits:
            key_int.append(int(charc))
        else:
            continue
    return key_int


# END