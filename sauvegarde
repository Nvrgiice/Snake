import time
#from programme_jeu import score  # on récupère le score 
#from programme_jeu import pseudo 
#gerer distance


def donnees():
    pseudo = input("Quelle est votre pseudo : ")  # Créer le pseudo du joueur
    score=15
    try:
        with open("score.txt", "a") as fichier:  # Utilisation du mode "a" pour ajouter des données à la fin du fichier
            fichier.write(f"{pseudo} / {score}")  # Écrire le pseudo du joueur et son score dans le fichier
    except Exception as e: #gérer les exceptions
        print(f"Une erreur s'est produite lors de l'enregistrement du pseudo : {e}")

def chronometre():
    debut = time.time()
    input("Appuyez sur Entrée pour démarrer le jeu...")
    input("Appuyez sur Entrée pour arrêter le jeu...")
    fin = time.time()
    duree_jeu = round(fin - debut,3)
    # Voir comment "réduire" le nombre de chiffres après la virgule
    try:
        with open("score.txt", "a") as fichier:
            fichier.write(f" / {duree_jeu}\n")
    except Exception as e:
        print(f"Une erreur s'est produite lors de l'enregistrement de la durée de jeu : {e}")


def classement():
    try:
        scores = []  # Tableau pour stocker les scores

        with open("score.txt", "r") as sc:
            for ligne in sc:
                donnees = ligne.strip().split(" / ")
                
            
                pseudo = donnees[0].strip()  # Récupère le pseudo du joueur
                score = int(donnees[1].strip())  # Récupère le score du joueur
                temps = round(float(donnees[2].strip()),3)  # Récupère le temps du joueur
                scores.append((pseudo, score, temps))  # Ajoute le pseudo/score/temps au tableau
        # Récupère les données du dernier joueur dans le fichier
        dernier_score = scores[-1][1]
        pseudo_dernier = scores[-1][0]
        dernier_temps = scores[-1][2]

        # Trie d'abord par score, puis par temps en cas d'égalité de score
        scores.sort(key=lambda x: (x[1], x[2]), reverse=True)

        # Affiche le classement des meilleurs scores
        print("Classement des meilleurs scores :")
        for i, (pseudo, score, temps) in enumerate(scores[:5], start=1):  # Affiche les cinq meilleurs scores avec leur pseudo et temps
            print(f"{i}. Joueur : {pseudo} - Score : {score} - Temps : {temps} secondes")

        #Afficher le pseudo le score et le temps du dernier joueur
        print(f"Votre score, {pseudo_dernier}, est de : {dernier_score} avec un temps de {dernier_temps} secondes")

        # Affiche un message en fonction du score du joueur
        if dernier_score < 5: 
            print("Continuez à vous entraîner ! Chaque partie est une opportunité d'améliorer votre performance.")
        elif dernier_score > 30:
            print("Félicitations ! Vous avez réalisé un score exceptionnel !")
        else:
            print("Continuez sur cette lancée !")
    
    except FileNotFoundError:
        print("Aucun score enregistré.")
    except Exception as e:
        print(f"Une erreur s'est produite lors de la lecture du fichier : {e}")

# Appel des fonctions pour les exécuter
donnees()
chronometre()
classement()

