import time
from programme_jeu import play
from tkinter import *
from tkinter import simpledialog


def donnees():
    pseudo = simpledialog.askstring("Pseudo", "Quel est votre pseudo ?", parent=fenetre)
    if pseudo:
        print("Pseudo saisi :", pseudo)
        infos(pseudo)
        classement()
    else:
        print("Aucun pseudo saisi")
        pseudo = "Anonyme"


def infos(pseudo):
    score = 15  # Score par défaut
    distance = 222  # distance par défaut .
    temps = 555555

    try:
        with open("score.txt", "a") as fichier:
            fichier.write(f"{pseudo} / {score} / {temps} / {distance}\n")  # Écrit le pseudo/ le score et la distance dans le fichier
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
                temps = float(donnees[2].strip())  # Récupère le temps du joueur
                distance = int(donnees[3].strip())  # Récupère la distance du joueur
                temps_minutes = int(temps // 60)  # Conversion en minutes
                temps_secondes = int(temps % 60)  # Conversion en secondes
                scores.append((pseudo, score, temps_minutes, temps_secondes, distance))  # Ajoute le pseudo/score/temps/distance au tableau

        # Récupère les données du dernier joueur dans le fichier
        dernier_score = scores[-1][1]
        pseudo_dernier = scores[-1][0]
        dernier_temps_minutes = scores[-1][2]
        dernier_temps_secondes = scores[-1][3]
        derniere_distance = scores[-1][4]

        # Trie d'abord par score, puis par temps en cas d'égalité de score et enfin par la distance en cas d'égalité
        scores.sort(key=lambda x: (x[1], x[2], x[3], x[4]), reverse=True)

        # Affiche le classement des meilleurs scores
        classement_text = "Classement des meilleurs scores :\n"
        for i, (pseudo, score, temps_minutes, temps_secondes, distance) in enumerate(scores[:5], start=1):
            classement_text += f"{i}. Joueur : {pseudo} - Score : {score} - Temps : {temps_minutes} min {temps_secondes} sec - Distance : {distance}\n"

        # Affiche un message en fonction du score du joueur
        if dernier_score < 5:
            message = "Continuez à vous entraîner ! Chaque partie est une opportunité d'améliorer votre performance."
        elif dernier_score > 30:
            message = "Félicitations ! Vous avez réalisé un score exceptionnel !"
        else:
            message = "Continuez sur cette lancée !"

        # Création de la fenêtre Tkinter pour afficher les résultats
        fenetre_resultats = Tk()
        fenetre_resultats.title("Résultats")
        fenetre_resultats.geometry("500x400")
        fenetre_resultats.config(bg="#B0E1B0")

        # Cadre pour le classement
        cadre_classement = Frame(fenetre_resultats, bg="#FFFFFF", bd=5)
        cadre_classement.pack(pady=10)

        # Étiquette pour afficher le classement
        label_classement = Label(cadre_classement, text=classement_text, bg="#FFFFFF", justify="left", font=("Arial", 12))
        label_classement.pack()

        # Étiquette pour afficher le message en fonction du score du joueur
        label_message = Label(fenetre_resultats, text=message, bg="#B0E1B0", font=("Arial", 12))
        label_message.pack(pady=10)

        fenetre_resultats.mainloop()

    except FileNotFoundError:
        print("Aucun score enregistré.")
    except Exception as e:
        print(f"Une erreur s'est produite lors de la lecture du fichier : {e}")


# Création de la fenêtre principale
fenetre = Tk()
fenetre.title("Pop-up pseudo")
fenetre.geometry("300x300")
fenetre.config(bg='#B0E1B0')  # Couleur de fond verte
fenetre.iconbitmap("snake.ico")

# Création d'un bouton pour déclencher la boîte de dialogue
bouton = Button(text="Entrer Pseudo", command=donnees)
bouton.pack(pady=10)  #

fenetre.mainloop()
