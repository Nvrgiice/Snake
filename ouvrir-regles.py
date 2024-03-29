from tkinter import Toplevel

# Fonction pour ouvrir la page des règles du jeu
def ouvrir_regles():
    # Création de la fenêtre des règles
    fenetre_regles = Toplevel()
    fenetre_regles.title("Règles du Jeu")
    fenetre_regles.geometry("400x300")
    fenetre_regles.config(background='#B0E1B0')

    # Texte des règles
    regles_texte = """
    Règles du Jeu :
    1. Utilisez les touches fléchées pour déplacer le serpent.
    2. Mangez les pommes pour grandir.
    3. Évitez de vous heurter aux murs ou à votre propre corps.
    4. Essayez de réaliser le meilleur score possible !
    """

    # Affichage des règles
    label_regles = Label(fenetre_regles, text=regles_texte, font=("Arial", 12), bg='#B0E1B0')
    label_regles.pack(padx=20, pady=20)

# Exemple d'utilisation de la fonction ouvrir_regles()
ouvrir_regles()
