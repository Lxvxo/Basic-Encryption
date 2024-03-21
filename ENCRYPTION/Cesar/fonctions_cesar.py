# coding: utf-8
"""
Auteur : Zodiac
Date : 24/11/2022
Objectif générale: Chiffrer ou Déchiffrer un message en code César
Objectif du fichier : Stocker les fonctions nécessaire au chiffrement César
"""
# BEGINNING

# Données nécessaires
char_divers: str = "0123456789" + "#$%&'()*+,-./:;<=>?@[\]^_`{|}~" + " "

# Fonctions


def cesar(text: str, key: int) -> str:
    """Chiffre un texte par la méthode César

    Args:
        text (str): Texte à chiffrer
        key (int): clé pour le chiffrage

    Returns:
        str : Texte chiffré en minuscule
    """
    text = text.lower()
    result: str = ""
    for k in range(len(text)):
        if text[k] in char_divers:
            result += text[k]
        else:
            indice : int = (ord(text[k]) + key - 97) % 26
            if indice < 0 : 
                indice += 26 
            result += chr(indice + 97)
    return result

def cesar_file(key: int, name_file: str) -> None:
    """Chiffre un fichier texte avec la méthode César

    Args:
        key (int): clé pour le chiffrement
        name_file (str): chemin du fichier relatif ou absolu du fichier
    """
    result: str = ""
    with open(name_file, "r") as file_read:
        list_lines: list[str] = file_read.read().split("\n")
        for line in list_lines:
            result += cesar(line, key)
            result += "\n"
    with open(name_file, "w") as file_write:
        file_write.write(result)


def transform_key(key: int, method: int) -> int:
    """Choisis la clé adéquate pour un chiffrement ou déchiffrement

    Args:
        key (int): clé pour le chiffrement
        method (int): 1 pour chiffrement | 0 pour déchiffrement

    Returns:
        int: key pour chiffrement | -key pour chiffrement
    """
    if method == 1:
        return key
    if method == 0:
        return -key


# END
