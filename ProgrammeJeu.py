from tkinter import *
from random import randint
import math 

# Création d’une "fenêtre"
fenetre = Tk()
fenetre.title("Snake")
fenetre.iconbitmap("snake.ico")
w, h = fenetre.winfo_screenwidth(), fenetre.winfo_screenheight()
fenetre.geometry("%dx%d" % (w, h))
fenetre.config(background='#288352')

#pour pleine écran
#fenetre.attributes('-fullscreen', 2)
#fenetre.bind('<Escape>',lambda e: fenetre.destroy())

#variable selon taille de écran
PGCD = math.gcd(fenetre.winfo_screenwidth() , fenetre.winfo_screenheight())
C = int(PGCD/3)    #côté de carreau
colonne = int(fenetre.winfo_screenwidth()//C)
ligne = int((fenetre.winfo_screenheight()-5*C)//C)

# Créaction Caneva
can = Canvas(fenetre,bg='yellow',height=C*ligne ,width=fenetre.winfo_screenwidth())
can.pack(side=BOTTOM)
#can.place()


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

creation_terrain()


#génération de pomme au hazard
def pomme():
    ligne_rand = randint(1, ligne)
    colone_rand = randint(1, colonne)
    monImage = PhotoImage(file="pomme.png").subsample(10)
    images.append(monImage)  # Garder une référence à l'image
    can.create_image(colone_rand * C - C//2, ligne_rand * C - C//2, image=monImage)

    
    return colone_rand * C - C//32, ligne_rand * C - C//2

images = []
x_pomme, y_pomme = pomme()


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


#=========================================================================================

ecb = int(C//8) #espace cercle bord

def mouvement():
    global Serpent
    i=len(Serpent)-1
    j=0
    while i > 0:
        Serpent[i][0]=Serpent[i-1][0]    #transmet l'abscisse au cercle avant
        Serpent[i][1]=Serpent[i-1][1]    #transmet l'aordonnée au cercle avant
        can.create_oval(Serpent[i][0]-3*ecb, Serpent[i][1]-3*ecb, Serpent[i][0]+3*ecb, Serpent[i][1]+3*ecb,outline='green', fill='black',) 
        i -= 1
    


    if direction  == 'gauche':
        Serpent[0][0]  = Serpent[0][0] - dx
        if Serpent[0][0] < 0:
            Serpent[0][0] = fenetre.winfo_screenwidth()-C//2
    elif direction  == 'droite':
        Serpent[0][0]  = Serpent[0][0] + dx
        if Serpent[0][0] > fenetre.winfo_screenwidth():
            Serpent[0][0] = C//2
    elif direction  == 'haut':
        Serpent[0][1]  = Serpent[0][1] - dy
        if Serpent[0][1] < 0:
            Serpent[0][1] = C*ligne-C//2
    elif direction  == 'bas':
        Serpent[0][1]  = Serpent[0][1] + dy
        if Serpent[0][1] > C*ligne:
            Serpent[0][1] = C//2
    can.create_oval(Serpent[i][0]-3*ecb, Serpent[i][1]-3*ecb, Serpent[i][0]+3*ecb, Serpent[i][1]+3*ecb,outline='green', fill='blue')
    
    soutient(Serpent[i-1][0],Serpent[i-1][1]) 
    test_pomme()
    #test_que(i)


    if flag != 0:
        fenetre.after(200, mouvement)   # temps 
    
    #can.create_image(x_pomme, y_pomme, image='pomme.png')

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
    
def test_pomme():
    global pomme
    global x,y,x_pomme,y_pomme
    global Serpent
    if Serpent[1][0]>x_pomme-C//2 and  Serpent[1][0]<x_pomme+C//2:        
        if Serpent[1][1]>y_pomme-C//2 and Serpent[1][1]<y_pomme+C//2:
            soutient(x_pomme+1-C//2,y_pomme)
            images = []
            x_pomme, y_pomme = pomme()
            Serpent.append([0,0]) #On joute un nouveau point au serpent

"""def test_que(i):
    a = len(Serpent)-1
    while a > 0 :
        if Serpent[i][0] == Serpent[a][0] and Serpent[i][1] == Serpent[a][1]:
            can.delete("all")    
    a-=1"""



flag = 1
dx = C
dy = C
direction = 'haut'
fenetre.bind('<d>', droite)
fenetre.bind('<q>', gauche)
fenetre.bind('<z>' , haut)
fenetre.bind('<s>', bas)
#==========================================================================================

x=3*C + C//2
y=3*C + C//2
Serpent=[[x,y],[x,y],[x,y],[x,y]]

mouvement()





fenetre.mainloop()
#pygame

