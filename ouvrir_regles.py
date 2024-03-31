from tkinter import Toplevel, Label 
from tkinter import *

# Fonction pour ouvrir la page des règles du jeu
def ouvrir_regles(fenetre, callback):
    # Création de la fenêtre des règles
    #fenetre_regles = Toplevel()
    #fenetre_regles.title("Règles du Jeu")
    #fenetre_regles.geometry("400x300")
    #fenetre_regles.config(background='#B0E1B0')

    # Texte des règles
    regles_texte = """
    Règles du Jeu :
    1. Utilisez les touches fléchées pour déplacer le serpent.
    2. Mangez les pommes pour grandir.
    3. Évitez de vous heurter aux murs ou à votre propre corps.
    4. Essayez de réaliser le meilleur score possible !
    """

    # Affichage des règles
    label_regles = Label(fenetre, text=regles_texte, font=("Arial", 12), bg='#B0E1B0')
    label_regles.pack(padx=20, pady=20)

    # bouton retour
    cadre_bouton_retour = Canvas(fenetre, width=150, height=50, bg="#C51C3D", highlightthickness=2, highlightbackground="black", bd=0, relief="flat", borderwidth=0, highlightcolor="black")
    cadre_bouton_retour.place(relx=0.5, rely=0.75, anchor=S)
    cadre_bouton_retour.create_text(75, 25, text="RETOUR", font=("Comic Sans MS", 20, "bold"), fill="white")

    cadre_bouton_retour.bind("<Button-1>", lambda _: callback('acceuil'))
 

