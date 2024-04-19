import time
#from programme_jeu import play  # on récupère le score le temps et la distance
#from pop_up_pseudo import donnees
from tkinter import *
from tkinter import simpledialog


def donnees():
    pseudo = simpledialog.askstring("Pseudo", "Quel est votre pseudo ?", parent=fenetre)
    if pseudo:
        print("Pseudo saisi :", pseudo)
    else:
        print("Aucun pseudo saisi")
        pseudo="Anonyme"
    return pseudo
# Création de la fenêtre principale
fenetre = Tk()
fenetre.title("Pop-up pseudo")
fenetre.geometry("300x300")
fenetre.config(bg='#B0E1B0')  # Couleur de fond verte
fenetre.iconbitmap("snake.ico")
image = fenetre.iconbitmap("snake.ico")



# Création d'un bouton pour déclencher la boîte de dialogue
bouton = Button(text="Entrer Pseudo", command=donnees)
bouton.pack(pady=10)  # Ajout d'un espacement en y pour centrer verticalement le bouton
bouton.place(x=100, y=130)




def infos():

    pseudo = donnees()
    score = 15  # Score par défaut
    distance = 222 #distance par défaut .
    temps = 555555
    #(score, distance, temps ) = play() 

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
                temps = round(float(donnees[2].strip()),3)  # Récupère le temps du joueur
                distance = int(donnees[3].strip()) #Récupère la distance du joueur
                scores.append((pseudo, score, temps, distance))  # Ajoute le pseudo/score/temps/distance au tableau

        # Récupère les données du dernier joueur dans le fichier
        dernier_score = scores[-1][1]
        pseudo_dernier = scores[-1][0]
        dernier_temps = scores[-1][2]
        derniere_distance = scores[-1][3]

        # Trie d'abord par score, puis par temps en cas d'égalité de score et enfin par la distance en cas d'égalité
        scores.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)

        # Affiche le classement des meilleurs scores
        print("Classement des meilleurs scores :")
        for i, (pseudo, score, temps, distance) in enumerate(scores[:5], start=1):  # Affiche les cinq meilleurs scores avec leur pseudo,temps et distance
            print(f"{i}. Joueur : {pseudo} - Score : {score} - Temps : {temps} secondes - Distance : {distance} ")

        #Afficher le pseudo le score le temps et la distance du dernier joueur
        print(f"Votre score, {pseudo_dernier}, est de : {dernier_score} avec un temps de {dernier_temps} secondes, pour une distance de {derniere_distance}")


        # Affiche un message en fonction du score du joueur

        if dernier_score < 5: 
            print("Continuez à vous entraîner ! Chaque partie est une opportunité d'améliorer votre performance.")

        elif dernier_score > 30:
            print("Félicitations ! Vous avez réalisé un score exceptionnel !")

        else:
            print("Continuez sur cette lancée !")

            #Ajout pour faire une pause pour lire les scores 
            time.sleep(5)

            #Avant de fermer le programme 
            quit()

# gerer les exceptions 

    except FileNotFoundError: 
        print("Aucun score enregistré.")
    except Exception as e:
        print(f"Une erreur s'est produite lors de la lecture du fichier : {e}")

# Appel des fonctions pour les exécuter

infos()
classement()
fenetre.mainloop()
