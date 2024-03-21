# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 20:09:34 2022

@author: Livio ss

Objectif : Apprendre Tkinter

"""
#image = PhotoImage(file="password.jpg") il faut convertir en format png

# ou utiliser la bibliothèque PIL 

#image = ImageTk.PhotoImage(Image.open("password.jpg")) 

# ou le mettre en format gif

# une fois l'erreur dans la console il faut la redémarrer

# import os
# print("Current working directory:", os.getcwd())

# from PIL import ImageTk, Image

import string # pour avoir tous les caractères

from random import randint, choice

def generate_password():# définie la fonction qui génère le mot de passe
    password_min = 8
    password_max = 16
    all_chars = string.ascii_letters + string.punctuation + string.digits
    password = "".join(choice(all_chars) for k in range(randint(password_min,password_max))) # on choisit à chaque tour de boucle element au hasard et on joint le tout
    password_entry.delete(0,END) # rend l'entrée vide
    password_entry.insert(0, password) # ajoute password à l'entrée


from tkinter import *
# créer la fenetre

window = Tk()

window.title("Générateur de mot de passe")
window.geometry("720x480")
window.iconbitmap("mdp.ico")
window.config(background = "#4065A4") #bleu

# créer la frame principale
frame = Frame(window, bg ="#4065A4")


# creation d'une image

width = 300 #longueur en pixels
height = 300 # hauteur en pixels

img = PhotoImage(file="cadenas.png")#.zoom(35).subsample(32)# gérer le zoom

canvas = Canvas(frame, width = width, height = height, bg ='#4065A4', bd = 0, highlightthickness = 0) # espace pour dessiner
canvas.create_image(width/2,height/2, image = img) # on place l'image au milieu du canvas
canvas.grid(row=0, column=0, sticky=W) # au lieu d'utiliser une methode pack on utilise grid, le sticky permet de ou l'image va etre placé par raport au nord est etc

# crer une sous boite
right_frame = Frame(frame, bg = "#4065A4")



# creer un titre
label_title = Label(right_frame, text = 'Mot de passe', font=('Helvetica',20, "bold"), bg = "#4065A4", fg ="white")
label_title.pack()

# creer un champs/entree/input
password_entry = Entry(right_frame, font=('Helvetica',20, "bold"), bg = "#4065A4", fg ="white")
password_entry.pack()

# creer le bouton pour generer le mot de passe
generator_password_button = Button(right_frame, text = "Générer",font=('Helvetica',20, "bold"), bg = "#4065A4", fg ="white", command = generate_password)
generator_password_button .pack(fill = X)


#on place la sous boite à droite de la frame principal
right_frame.grid(row=0, column=1,sticky=W)

#afficher la frame
frame.pack(expand=True)



# creation d'une barre de menu
menu_bar = Menu(window)
#créer un premier menu
file_menu = Menu(menu_bar, tearoff =0)
file_menu.add_command(label = "Nouveau", command = generate_password)
file_menu.add_command(label = "Quitter", command = window.destroy)

menu_bar.add_cascade(label="Fichier", menu=file_menu)

# configurer notre fenetre pour ajouter notre menu bar
window.config(menu = menu_bar)


# afficher la fenetre
window.mainloop()
