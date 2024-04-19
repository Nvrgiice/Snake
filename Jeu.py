from tkinter import *
from random import *
import math 
import time


def initialisation():

    global distance, score, fenetre, w, h, point2, distance2, temps2, C, colonne, ligne, can, ecb, flag, dx, dy, direction, x, y, Serpent, temps_début

    distance = 0  # initialisation de la distance
    score = 0     # initialisation du score (nombre de point)

    # Création d’une "fenêtre"
    fenetre = Tk()
    fenetre.title("Snake")                                             # titre de la fennêtre
    fenetre.iconbitmap("snake.ico")                                    # logo du programme
    w, h = fenetre.winfo_screenwidth(), fenetre.winfo_screenheight()   # longeur, largeur
    fenetre.geometry("%dx%d" % (w, h))                                 # fenêtre de taille de l'écrans
    fenetre.config(background='#288352')                               # couleur

    cadreO = Frame(fenetre, bg='#288352')                              # cadre possédant les autres cadres : 1, 2, 3
    cadre1 = Frame(cadreO, bg='#3396ff', bd=5, relief=SUNKEN)          # cadre pour les points
    cadre2 = Frame(cadreO, bg='#3396ff', bd=5, relief=SUNKEN)          # cadre pour la distance
    cadre3 = Frame(cadreO, bg='#3396ff', bd=5, relief=SUNKEN)          # cadre pour le temps


    point1 = Label(cadre1, text = "Point(s) : ", font="Calibri, 15", fg='pink', bg='#3396ff')       # écriture du cadre 1
    point1.pack()                                                                                   # écriture en haut du cadre 1
    point2 = Label(cadre1, text = f"{0}", font="Calibri, 10", fg='pink', bg='#3396ff')              # initialisation de la valeur de point
    point2.pack()                                                                                   # position en bas du cadre 1

    distance1 = Label(cadre2, text = "Distance :", font="Calibri, 15", fg='pink', bg='#3396ff')     # écriture en haut du cadre 2
    distance1.pack()                                                                                # écriture en haut du cadre 2
    distance2 = Label(cadre2, text = f"{0}", font="Calibri, 10", fg='pink', bg='#3396ff')           # initialisation de la valeur de distance
    distance2.pack()                                                                                # position en bas du cadre 2

    temps1 = Label(cadre3, text = "Temps :", font="Calibri, 15", fg='pink', bg='#3396ff')           # écriture en haut du cadre 3
    temps1.pack()                                                                                   # écriture en haut du cadre 2
    temps2 = Label(cadre3, text = f"{0}min ; {0}s", font="Calibri, 10", fg='pink', bg='#3396ff')    # initialisation de la valeur de temps
    temps2.pack()                                                                                   # position en bas du cadre 3


    #variable selon taille de écran
    PGCD = math.gcd(w , h)     #détermination du PGCD en fonction de la longueur et de la largeur
    C = int(PGCD/3)            #côté de carreau
    colonne = int(w//C)        #détermination du nombre de colonne sur le terrain en fonction de la dimension des carreau
    ligne = int((h-5*C)//C)    #détermination du nombre de ligne sur le terrain en fonction de la dimension des carreau

    # Créaction Caneva
    can = Canvas(fenetre,bg='yellow',height=C*ligne ,width=C*colonne)   #création du canvas qui portera le jeu
    can.pack(side=BOTTOM)                                               #le canva sera situé en bas de la fenêtre

    #palce les compteur de point, ditance et temps à un espace régulier déterminer par la largeur de la fenêtre
    cadre1.pack(side=LEFT,padx=(w//10))
    cadre3.pack(side=RIGHT,padx=(w//10))
    cadre2.pack(expand=YES,padx=(w//10))
    cadreO.pack(pady=10)                    #les compteur de point, ditance et temps à 10 pixel du bord haut

    ecb = int(C//8)         #espace cercle bord (du carreaux)

    flag = 1                #valeur indiquant lorsque la partie est perdu (si = 0)
    dx, dy = C, C           #valeur d'un pas en absice ou ordonnée

    direction = 'bas'                    #initialisation de la direction en bas
    x, y = 6*C + C//2 , 6*C + C//2       #initialisation des valeur de x et y
    Serpent=[[x,y],[x,y-C],[x,y-2*C]]    #initialisation de la position du serpent

    temps_début = time.time()

#======================================programme principale====================================================


def mouvement():
    global Serpent
    global distance, score, temps
    global flag

    can.delete("corps")      # efface le corps précédent
    can.delete("tete")       # efface la tête précédente

    i=len(Serpent)-1         # nombre de morceau du serpent

    while i > 0:
        Serpent[i][0]=Serpent[i-1][0]                                                                                                                             # transmet l'abscisse au cercle avant
        Serpent[i][1]=Serpent[i-1][1]                                                                                                                             # transmet l'aordonnée au cercle avant
        can.create_oval(Serpent[i][0]-3*ecb, Serpent[i][1]-3*ecb, Serpent[i][0]+3*ecb, Serpent[i][1]+3*ecb,outline='green', fill='black',tags = 'corps')          # créer le corps du serpend (sans la tête)
        i -= 1


    if direction  == 'gauche':                  # si la commande de déplacement vérifie gauche
        Serpent[0][0]  = Serpent[0][0] - dx     # déplace la tête à gauche (-dx), le reste du serpend suivra
        if Serpent[0][0] < 0:                   # si touche le bord gaucher 
            Serpent[0][0] = w-C//2              # apparait au bord droit

    elif direction  == 'droite':                # si la commande de déplacement vérifie droite
        Serpent[0][0]  = Serpent[0][0] + dx     # déplace la tête à droite (+dx), le reste du serpend suivra
        if Serpent[0][0] > w:                   # si touche le bord droit
            Serpent[0][0] = C//2                # apparait au bord gauche

    elif direction  == 'haut':                  # si la commande de déplacement vérifie haut
        Serpent[0][1]  = Serpent[0][1] - dy     # déplace la tête en haut (-dy), le reste du serpend suivra
        if Serpent[0][1] < 0:                   # si touche le bord haut
            Serpent[0][1] = C*ligne-C//2        # apparait au bord bas

    elif direction  == 'bas':                   # si la commande de déplacement vérifie bas
        Serpent[0][1]  = Serpent[0][1] + dy     # déplace la tête en bas (+dy), le reste du serpend suivra
        if Serpent[0][1] > C*ligne:             # si touche le bord bas
            Serpent[0][1] = C//2                # apparait au bord haut
    
    can.create_oval(Serpent[i][0]-3*ecb, Serpent[i][1]-3*ecb, Serpent[i][0]+3*ecb, Serpent[i][1]+3*ecb,outline='green', fill='blue', tags='tete')          # créer la tête du serpend

    score = test_pomme()
    test_pomme()   
    flag = test_perdu()
    
    temps_encours = time.time()

    distance += 1                     #incrémentatin du compteur de distance à chaque mouvement
    #temps = round(distance*0.150,3)   #calcule la 

    temps = round(temps_encours-temps_début)

    
    apparition_donnée()


    if flag != 0:                                                #si condition d'erreur non vérifier
        fenetre.after(150,mouvement)   # temps 
        #return distance, score

    else :                                                       #si condition d'erreur vérifier
        print(f"dans mouvement {distance} {score}")
        return distance, score



    

#========================================programme appeller dans le programme principale==========================

def gauche(event):           # fonction qui détermine la direction = gauche si appeler
    global direction
    direction = 'gauche'
 
def droite(event):           # fonction qui détermine la direction = droite si appeler
    global direction
    direction = 'droite'
 
def haut(event):             # fonction qui détermine la direction = haut si appeler
    global direction
    direction = 'haut'
 
def bas(event):              # fonction qui détermine la direction = bas si appeler
    global direction
    direction = 'bas'


def creation_terrain():      # fonction qui créer le terrain

    #les carreau serons de longueur et de largeur C (PGCD divisé par 3)
    x_début = 0
    y_début = 0
    x_fin = C
    y_fin = C

    for i in range (0,colonne):  
        t = i                                                                                  # la variable t permet d'alterner les deux couleur possible de carreau
        for j in range (0,ligne) :
            if t%2 == 1 :
                couleur = '#32c258'                                                            # vert foncée (adapté au terrain)
            else :
                couleur = 'light green'                                                        # vert claire
            t+=1                                                                               # permet d'alternation grâce à l'incrémentation
            carrée = can.create_rectangle(x_début,y_début,x_fin,y_fin,width=1,fill=couleur)    # créer les carreau
            y_début += C                                                                       #
            y_fin += C
        
        y_début = 0
        y_fin = C
        x_début += C
        x_fin += C

def pomme():                                   #génération de pomme au hazard
    ligne_rand = randint(1, ligne)
    colone_rand = randint(1, colonne)
    # est-ce que la case ligne_rand,colone_rand appartient au snake ?
    # si oui
    # relancer pomme()
    # sinon code suivant
    monImage = PhotoImage(file="pomme.png").subsample(10)
    images.append(monImage)  # Garder une référence à l'image
    can.create_image(colone_rand * C - C//2, ligne_rand * C - C//2, image=monImage)

    return colone_rand * C - C//32, ligne_rand * C - C//2

def soutient(x,y):
    m = int(x//C)
    o = int(y//C)
    if m%2 == 0 :
        if o%2 == 0 : 
            carrée = can.create_rectangle(x-C//2,y-C//2,x+C//2,y+C//2,width=1,fill='light green')
            #claire
        else :
            carrée = can.create_rectangle(x-C//2,y-C//2,x+C//2,y+C//2,width=1,fill='#32c258')
            #foncée
    
    else :
        if o%2 == 0 : 
            carrée = can.create_rectangle(x-C//2,y-C//2,x+C//2,y+C//2,width=1,fill='#32c258')
            #foncée
        else :
            carrée = can.create_rectangle(x-C//2,y-C//2,x+C//2,y+C//2,width=1,fill='light green')
            #claire


def test_pomme():
    global pomme
    global x,y,x_pomme,y_pomme
    global Serpent
    global score

    if Serpent[1][0]>x_pomme-C//2 and  Serpent[1][0]<x_pomme+C//2:        
        if Serpent[1][1]>y_pomme-C//2 and Serpent[1][1]<y_pomme+C//2:
            soutient(x_pomme+1-C//2,y_pomme)
            images = []
            x_pomme, y_pomme = pomme()
            Serpent.append([0,0])                                           #On joute un nouveau point au serpent
            score += 1

    return score


def test_perdu():
    global x,y
    global Serpent, flag
    t = len(Serpent)-1
    while t > 0:
        if Serpent[0][0]>Serpent[t][0]-C//2 and  Serpent[0][0]<Serpent[t][0]+C//2:        
            if Serpent[0][1]>Serpent[t][1]-C//2 and Serpent[0][1]<Serpent[t][1]+C//2:
                flag = 0
                popup_perdu()

                return flag
        t-=1

def popup_perdu() :
    fen_perdu = Toplevel()
    fen_perdu.iconbitmap("snake.ico")
    fen_perdu.config(background='#1d7677')
    fen_perdu.title('Erreur')
    fen_perdu.geometry("400x200+400+400") # +400 + 400 : permet de positionner le popup sur l'écran - en partant du coin en haut à gauche
    message = Label(fen_perdu, text="Perdu !!", fg="#6ef31d", bg="#1d7677", font='Calibri 30 bold')
    message.pack()

    cadre = Frame(fen_perdu, background='#1d7677')

    btAjouter = Button(cadre, text = "Rejouer", width=10, height=1)
    btVider = Button(cadre, text = "Retour vers menu", width=15, height=1)
    btQuitter = Button(cadre, text = "Quitter", width=10, height=1, command=fenetre.destroy)

    btAjouter.pack(side=LEFT, padx=10)
    btQuitter.pack(side=RIGHT, padx=10)
    btVider.pack(padx=10)

    cadre.pack(expand=YES)


def apparition_donnée():
    global distance , score, temps
    point2.configure(text=score)
    distance2.configure(text=distance)
    temps2.configure(text=f"{int(temps//60)}min ; {int(temps%60)}s")


#=============================caractère permmetant de contrôler la direction=======================================

def dir() :
    fenetre.bind('<d>', droite)     # si touche d appuyer appelle la fonction droite
    fenetre.bind('<q>', gauche)     # si touche q appuyer appelle la fonction gauche
    fenetre.bind('<z>' , haut)      # si touche z appuyer appelle la fonction haut
    fenetre.bind('<s>', bas)        # si touche s appuyer appelle la fonction bas

#========================================fonction qui appelle tout=================================================


def play():
    temps_début = time.time()
    global images
    global x_pomme, y_pomme
    global distance , score

    initialisation()
    creation_terrain()
    images = []
    x_pomme, y_pomme = pomme()
    mouvement()                                         # La fonction continue alors que mouvement encore actif
    dir()
    print(time.time())
    print(" distance: ", distance, "score", score)
    



play()



fenetre.mainloop()
