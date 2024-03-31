# code page accueil
# Import des noms du module
from tkinter import *
from pages import *

# Création d'un objet "fenêtre"
fenetre = Tk()

# Titre de la fenêtre
fenetre.title("Snake - Acceuil")

# Taille de la fenêtre
 
w, h = fenetre.winfo_screenwidth(), fenetre.winfo_screenheight()
fenetre.geometry(f"{w}x{h}")

# Récupération d'une image pour changer le logo par défaut
#fenetre.iconbitmap("logo.ico1.png")

# Modification de la couleur du fond de la fenêtre
fenetre.config(background='#B0E1B0')

page_actuel = 'acceuil' # creation de la variable qui est la page actuel

def changer_page(nouvelle_page): 
    global page_actuel # on veut que cette variable change dans tout le code
    page_actuel = nouvelle_page

# enlever les éléments de la fenetre
    for widget in fenetre.winfo_children():
        widget.destroy()
    if page_actuel == 'acceuil' : 
        afficher_acceuil(fenetre, changer_page)
    if page_actuel == 'regles':
        ouvrir_regles(fenetre, changer_page)

changer_page(page_actuel)

# Démarrage de la boucle Tkinter (à placer à la fin !!!)
fenetre.mainloop()

