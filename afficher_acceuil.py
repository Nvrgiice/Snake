# code page accueil
# Import des noms du module
from tkinter import *


def afficher_acceuil(fenetre, callback):
    global image_snake # rendre cette variable globale

    #suppr_fenetre()
    
    # Titre (Label)
    image_snake = PhotoImage(file="snake_image.png")  # Assurez-vous d'avoir un fichier image nommé "snake_image.png" dans le même répertoire que votre script
    # Affichage de l'image
    label_image = Label(fenetre, image=image_snake, bg='#B0E1B0')
    label_image.pack()
    # Affichage du titre

    #bouton play 
    cadre_bouton_play = Canvas(fenetre, width=150, height=50, bg="#C51C3D", highlightthickness=2, highlightbackground="black", bd=0, relief="flat", borderwidth=0, highlightcolor="black")
    cadre_bouton_play.place(relx=0.5, rely=0.75, anchor=S)
    cadre_bouton_play.create_text(75, 25, text="PLAY", font=("Comic Sans MS", 20, "bold"), fill="white")

    # Création du cadre pour le bouton "règles du jeu"
    cadre_bouton_regles = Canvas(fenetre, width=200, height=50, bg="#C51C3D", highlightthickness=2, highlightbackground="black", bd=0, relief="flat", borderwidth=0, highlightcolor="black")
    cadre_bouton_regles.place(relx=0.5, rely=0.85, anchor=S)

    # Création du texte "Règles du jeu" dans le cadre
    cadre_bouton_regles.create_text(100, 25, text="REGLES DU JEU", font=("Comic Sans MS", 16, "bold"), fill="white")

    # Associer la fonction ouvrir_regles() au clic sur le cadre "Règles du jeu"
    cadre_bouton_regles.bind("<Button-1>", lambda _: callback('regles')) # _ ignore argument
