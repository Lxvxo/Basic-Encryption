# coding: utf-8
"""
Auteur : Zodiac
Date : 26/11/2022
Objectif générale: Chiffrer ou Déchiffrer un message en code Vignère
Objectif du fichier : Stocker les fonctions nécessaire au chiffrement Vignère
"""
# BEGINNING

# Données nécessaires
char_divers: str = "0123456789" + "#$%&'()*+,-./:;<=>?@[\]^_`{|}~" + " "

# Fonctions

def charac_blocs(length_text : int , key : str ) -> str:
    """Définit les différents blocs sous la forme d'une seule chaine de charactères

    Args:
        length_text (int): taille du texte 
        key (str): la clé pour le chiffrement

    Returns:
        str: les différents blocs concaténés en chaine de charactère
    """
    key : str = key.lower()
    nb_blocs : int = length_text // len(key)
    add_blocs : int = length_text % len(key)
    add_charac : str = ""
    for charac in range(add_blocs):
        add_charac += key[charac]
    
    return nb_blocs*key + add_charac

def vignere(text : str, key: str , signe = 1) -> str:
    """Chiffre un message avec la méthode de Vignère

    Args:
        text (str): texte à chiffré
        key (int): clé pour le chiffrement
        signe (int, optional): 1 pour le chiffrement | -1 pour le déchiffrement. Defaults to 1.

    Returns:
        str: texte chiffré
    """
    list_blocs_str : str = charac_blocs(len(text), key)
    text : str = text.lower()
    result : str = ""
    for k in range(len(text)):
        if text[k] in char_divers:
            result += text[k]
        else:
            decalage = ord(list_blocs_str[k]) - 96
            indice : int = (ord(text[k]) + decalage*signe - 97) % 26
            if indice < 0 : 
                indice += 26 
            result += chr(indice + 97)
    return result

def vignere_file(key: str, name_file: str, signe : int) -> None:
    """Chiffre un fichier texte avec la méthode Vignere

    Args:
        key (str): clé pour le chiffrement
        name_file (str): chemin du fichier relatif ou absolu du fichier
        signe (int) : 1 pour le chiffrement | -1 pour le déchiffrement
    """
    result: str = ""
    with open(name_file, "r") as file_read:
        list_lines : list[str] = file_read.read().split("\n")
        for line in list_lines:
            result += vignere(line, key, signe)
            result += "\n"
    with open(name_file, "w") as file_write:
        file_write.write(result)

#END
        