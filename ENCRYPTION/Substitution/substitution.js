// coding: utf-8 

/* 
Auteur : Zodiac
Date : 24/11/2022
Objectif générale : Chiffrer ou Déchiffrer un message par Substitution
Objectif du fichier : 
 */

//BEGINNING

// Définition des variables globales
const alphabet = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

//Fonctions 

/**
 * mélange aléatoirement une liste
 * @param {Array.<object>} array 
 * @returns {Array.<object>}
 */
function shuffle(array) { 
    array.sort(() => Math.random() - 0.5)
    return array
}

/**
 * transforme un texte en liste de chiffre où chaque chiffre est associé à une lettre selon la table ASCII
 * @param {string} text
 * @returns {Array.<Integer>}
*/
function toInt(text) { 
    text = text.toLowerCase()
    var tmp = []
    for (var i = 0; i < text.length; i++) {
        if (text[i] === " ") {
            tmp.push(" ")
        }
        else {
            tmp.push(text.charCodeAt(i) - 97)
        }
    }
    return tmp
}

/**
 * crée une liste en associant chaque élément de tab à un élément de key (chiffrement)
 * @param {Array.<Integer>} tab
 * @param {Array.<Integer>} key
 * @returns {Array.<Integer>}
 */
function chiffrer(tab, key) { 
    var c = []
    for (var i = 0; i < tab.length; i++) {
        if (tab[i] === " ") {
            c.push(" ")
        }
        else {
            c.push(key[tab[i]])
        }

    }
    return c
}
/**
 * crée une liste en associant chaque élément de key à un élément de tab (déchiffrement)
 * @param {Array.<Integer>} tab
 * @param {Array.<Integer>} key
 * @returns {Array.<Integer>}
 */
function dechiffrer(tab, key) { 
    var c = []
    for (var i = 0; i < tab.length; i++) {
        if (tab[i] === " ") {
            c.push(" ")
        }
        else {
            c.push(key.indexOf(tab[i]))
        }

    }
    return c
}

/**
 * transforme une liste de chiffre en Str selon la table ASCII
 * @param {Array.<Integer>} tab
 * @returns {Array.<String>}
 */
function toStr(tab) { 
    result = []
    for (var i = 0; i < tab.length; i++) {
        if (tab[i] === " ") {
            result.push(" ")
        }
        else {
            result.push(String.fromCharCode(tab[i] + 97))
        }

    }
    return result
}

/**
 * Chiffre le texte sur la page HTML avec la méthode Substitution
 * @returns {None}
 */
function Substitution() { //Chiffre le texte avec la méthode Substitution
    var text = document.getElementById("text").value
    var key = list_str_to_list_int(document.getElementById("key").value.split(","))
    var text_crypte = toStr(chiffrer(toInt(text), key)).join("")
    document.getElementById("text_crypte").innerHTML = text_crypte

}
/**
 * Génère une clé de chiffrement
 * @returns {None}
 */
function Generate_key() { // 
    var key = shuffle(alphabet)
    document.getElementById("key").value = key.toString()
    Substitution()
    Check_cesar()
}
/**
 * Change la clé de chiffrement
 * @returns {None}
 */
function Change_key_manuel() {
    Substitution()
    Check_cesar()
}
/**
 * affiche la clé de chiffrement
 * @returns {None}
 */
function Show_key() { 
    document.getElementById("key").hidden = false
}
/**
 * cache la clé de chiffrement
 * @returns {None}
 */
function Hide_key() { 
    document.getElementById("key").hidden = true
}
/**
 * vérifie si la clé est associable à une clé césar
 * @param {Array.<Integer>} key
 * @returns {boolean}
 */
function condition_cesar(key) { 
    var verif = 0
    for (i = 0; i < key.length - 1; i++) {
        if (key[i + 1] != key[i] + 1) {
            verif += 1
        }
    }
    if (verif === 0 && key.length == 26) {
        return true
    }
    else {
        return false
    }

}
/**
 * affiche true si la clé est une clé césar et affiche false sinon
 * @returns {None}
 */
function Check_cesar() { 
    if (document.getElementById("check_cesar").checked) {
        document.getElementById("cesar").hidden = false
        document.getElementById("cesar").innerHTML = condition_cesar(list_str_to_list_int(document.getElementById("key").value.split(",")))
    }
    else {
        document.getElementById("cesar").hidden = true
        document.getElementById("cesar").innerHTML = ""
    }
}


/**
 * Déchiffre le texte avec la méthode Substitution
 * @returns {None}
 */
function Dechiffrement() { 
    var text = document.getElementById("text_2").value
    var key_2 = list_str_to_list_int(document.getElementById("key_2").value.split(","))
    var text_decrypte = toStr(dechiffrer(toInt(text), key_2)).join("")
    document.getElementById("text_decrypte").innerHTML = text_decrypte
}
/**
 * transforme une liste de str en liste de int
 * @param {Array.<String>} list
 * @returns {Array.<Integer>}
 */
function list_str_to_list_int(list) { 
    for (i = 0; i < list.length; i++) {
        list[i] = parseInt(list[i])
    }
    return list
}
//END
