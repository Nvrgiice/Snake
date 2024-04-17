from tkinter import *
from random import *
import math 
import time

distance = int(0)
score = int(0)

# Création d’une "fenêtre"
fenetre = Tk()
fenetre.title("Snake")
fenetre.iconbitmap("snake.ico")
w, h = fenetre.winfo_screenwidth(), fenetre.winfo_screenheight()
fenetre.geometry("%dx%d" % (w, h))
fenetre.config(background='#288352')

cadreO = Frame(fenetre, bg='#288352')
cadre1 = Frame(cadreO, bg='#3396ff', bd=5, relief=SUNKEN)
cadre2 = Frame(cadreO, bg='#3396ff', bd=5, relief=SUNKEN)
cadre3 = Frame(cadreO, bg='#3396ff', bd=5, relief=SUNKEN)

point1 = Label(cadre1, text = "Point : ", font="Calibri, 15", fg='pink', bg='#3396ff')
point1.pack()
point2 = Label(cadre1, text = "?", font="Calibri, 10", fg='pink', bg='#3396ff')
point2.pack()

distance1 = Label(cadre2, text = "Distance :", font="Calibri, 15", fg='pink', bg='#3396ff')
distance1.pack()
distance2 = Label(cadre2, text = "?", font="Calibri, 10", fg='pink', bg='#3396ff')
distance2.pack()

temps1 = Label(cadre3, text = "Temps :", font="Calibri, 15", fg='pink', bg='#3396ff')
temps1.pack()
temps2 = Label(cadre3, text = "?", font="Calibri, 10", fg='pink', bg='#3396ff')
temps2.pack()




#variable selon taille de écran
PGCD = math.gcd(w , h)   
C = int(PGCD/3)    #côté de carreau
reste_longeur = w%C
colonne = int(w//C)
ligne = int((h-5*C)//C)

# Créaction Caneva
can = Canvas(fenetre,bg='yellow',height=C*ligne ,width=C*colonne)
can.pack(side=BOTTOM)

cadre1.pack(side=LEFT,padx=(w//10))
cadre3.pack(side=RIGHT,padx=(w//10))
cadre2.pack(expand=YES,padx=(w//10))
cadreO.pack(pady=10)

#=========================================================================================

ecb = int(C//8) #espace cercle bord
distance = int(0)
score = int(0)

def mouvement():
    global Serpent
    global distance, score
    global flag
    

    can.delete("corps")
    can.delete("tete")

    i=len(Serpent)-1

    while i > 0:
        Serpent[i][0]=Serpent[i-1][0]    #transmet l'abscisse au cercle avant
        Serpent[i][1]=Serpent[i-1][1]    #transmet l'aordonnée au cercle avant
        can.create_oval(Serpent[i][0]-3*ecb, Serpent[i][1]-3*ecb, Serpent[i][0]+3*ecb, Serpent[i][1]+3*ecb,outline='green', fill='black',tags = 'corps') 
        i -= 1

    if direction  == 'gauche':
        Serpent[0][0]  = Serpent[0][0] - dx
        if Serpent[0][0] < 0:
            Serpent[0][0] = w-C//2
    elif direction  == 'droite':
        Serpent[0][0]  = Serpent[0][0] + dx
        if Serpent[0][0] > w:
            Serpent[0][0] = C//2
    elif direction  == 'haut':
        Serpent[0][1]  = Serpent[0][1] - dy
        if Serpent[0][1] < 0:
            Serpent[0][1] = C*ligne-C//2
    elif direction  == 'bas':
        Serpent[0][1]  = Serpent[0][1] + dy
        if Serpent[0][1] > C*ligne:
            Serpent[0][1] = C//2
    
    can.create_oval(Serpent[i][0]-3*ecb, Serpent[i][1]-3*ecb, Serpent[i][0]+3*ecb, Serpent[i][1]+3*ecb,outline='green', fill='blue', tags='tete')

    score = test_pomme()
    flag = test_perdu()
    
    distance += 1

    
    apparition_donnée(distance , score)

    if flag != 0:
        fenetre.after(150,mouvement)   # temps 
        #return distance, score

    else :
        print(f"dans mouvement {distance} {score}")
        return distance, score



def gauche(event):
    global direction
    direction = 'gauche'
 
def droite(event):
    global direction
    direction = 'droite'
 
def haut(event):
    global direction
    direction = 'haut'
 
def bas(event):
    global direction
    direction = 'bas'


def creation_terrain():
    x_début = 0
    y_début = 0
    x_fin = C
    y_fin = C
    for i in range (0,colonne):  
        t = i
        for j in range (0,ligne) :
            if t%2 == 1 :
                cc = '#32c258'
            else :
                cc = 'light green'
            t+=1
            carrée = can.create_rectangle(x_début,y_début,x_fin,y_fin,width=1,fill=cc)
            y_début += C
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
            Serpent.append([0,0]) #On joute un nouveau point au serpent
            score += 1

    return score

def test_perdu():
    global x,y
    global Serpent
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
    #fen_perdu.title('Erreur')
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


def apparition_donnée(distance , score):
    point2.configure(text=score)
    distance2.configure(text=distance)
    temps2.configure(text=round(distance*0.150,3))


flag = 1
dx = C
dy = C
direction = 'bas'
fenetre.bind('<d>', droite)
fenetre.bind('<q>', gauche)
fenetre.bind('<z>' , haut)
fenetre.bind('<s>', bas)

x=6*C + C//2
y=6*C + C//2
Serpent=[[x,y],[x,y-C],[x,y-2*C]]


def play():
    global images
    global x_pomme, y_pomme
    global distance , score

    creation_terrain()
    images = []
    x_pomme, y_pomme = pomme()
    mouvement()                         # La fonction continue alors que mouvement encore actif
    print(distance, score)

play()



fenetre.mainloop()
#pygame

#deiconify et withdraw
