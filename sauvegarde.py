import time
import tkinter as tk
from tkinter import simpledialog

def donnees():
    pseudo = simpledialog.askstring("Pseudo", "Quel est votre pseudo ?", parent=fenetre)
    if pseudo:
        print("Pseudo saisi :", pseudo)
    else:
        pseudo = "Anonyme"
    return pseudo

def infos():
    pseudo = donnees()
    score = 15  # Score par défaut
    distance = 222 #distance par défaut .
    temps = 555555
    #(score, distance, temps ) = play() 
    try:
        with open("score.txt", "a") as fichier:
            fichier.write(f"{pseudo} / {score} / {temps} / {distance}\n")
    except Exception as e:
        print(f"Une erreur s'est produite lors de l'enregistrement du pseudo et du score : {e}")

def classement():
    try:
        scores = []  # Tableau pour stocker les scores

        with open("score.txt", "r") as sc: 
            sc.readline()
            for ligne in sc:
                donnees = ligne.strip().split(" / ")
                pseudo = donnees[0].strip()  # Récupère le pseudo du joueur
                score = int(donnees[1].strip())  # Récupère le score du joueur
                temps = round(float(donnees[2].strip()), 3)  # Récupère le temps du joueur
                distance = int(donnees[3].strip()) # Récupère la distance du joueur
                scores.append((pseudo, score, temps, distance))  # Ajoute le pseudo/score/temps/distance au tableau

        # Récupère le pseudo, le score, le temps et la distance du dernier joueur
        # Fait avant de trier les infos récupérées dans le fichier des scores
        dernier_score = scores[-1][1]
        pseudo_dernier = scores[-1][0]
        dernier_temps = scores[-1][2]
        derniere_distance = scores[-1][3]
        
        scores.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)  # Trie les scores
        
        fenetre_classement = tk.Toplevel(fenetre)  # Crée une nouvelle fenêtre pour afficher le classement
        fenetre_classement.title("Classement des scores")

        cadre_classement = tk.Frame(fenetre_classement)  # Crée un cadre pour le classement
        cadre_classement.pack(padx=20, pady=20)

        # Affiche le classement des meilleurs scores
        label_classement = tk.Label(cadre_classement, text="Classement des meilleurs scores", font=("Arial", 14, "bold"))
        label_classement.grid(row=0, column=0, columnspan=2, pady=10)

        for i, (pseudo, score, temps, distance) in enumerate(scores[:5], start=1):
            label_info = tk.Label(cadre_classement, text=f"{i}. Joueur : {pseudo} - Score : {score} - Temps : {temps} secondes - Distance : {distance}", font=("Arial", 12))
            label_info.grid(row=i, column=0, columnspan=2, pady=5)

        # Affiche le pseudo, le score, le temps et la distance du dernier joueur
        label_dernier = tk.Label(cadre_classement, text=f"Votre score, {pseudo_dernier}, est de : {dernier_score} avec un temps de {dernier_temps} secondes, pour une distance de {derniere_distance}", font=("Arial", 12))
        label_dernier.grid(row=6, column=0, columnspan=2, pady=10)

        # Affiche un message en fonction du score du joueur
        if dernier_score < 5: 
            label_message = tk.Label(cadre_classement, text="Continuez à vous entraîner ! Chaque partie est une opportunité d'améliorer votre performance.", font=("Arial", 12))
            label_message.grid(row=7, column=0, columnspan=2, pady=5)
        elif dernier_score > 30:
            label_message = tk.Label(cadre_classement, text="Félicitations ! Vous avez réalisé un score exceptionnel !", font=("Arial", 12))
            label_message.grid(row=7, column=0, columnspan=2, pady=5)
        else:
            label_message = tk.Label(cadre_classement, text="Continuez sur cette lancée !", font=("Arial", 12))
            label_message.grid(row=7, column=0, columnspan=2, pady=5)

        # Ajoute un bouton "Retour" pour revenir à la fenêtre principale
        bouton_retour = tk.Button(fenetre_classement, text="Retour", command=fenetre_classement.destroy)
        bouton_retour.pack(pady=10)

    except FileNotFoundError: 
        print("Aucun score enregistré.")
    except Exception as e:
        print(f"Une erreur s'est produite lors de la lecture du fichier : {e}")

# Crée la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Pop-up pseudo")
fenetre.geometry("300x300")
fenetre.config(bg='#B0E1B0')  # Couleur de fond verte
fenetre.iconbitmap("snake.ico")

# Crée un bouton pour entrer le pseudo
bouton = tk.Button(text="Entrer Pseudo", command=donnees)
bouton.pack(pady=10)  # Ajout d'un espacement en y pour centrer verticalement le bouton
bouton.place(x=100, y=130)

# Appelle les fonctions pour les exécuter
infos()
classement()

# Affiche la fenêtre principale
fenetre.mainloop()

