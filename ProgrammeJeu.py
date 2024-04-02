from tkinter import *
from random import randrange


# Création d’une "fenêtre"
fenetre = Tk()
fenetre.title("Snake")
fenetre.iconbitmap("snake.ico")
w, h = fenetre.winfo_screenwidth(), fenetre.winfo_screenheight()
fenetre.geometry("%dx%d" % (w, h))
fenetre.config(background='#288352')



# Créaction Caneva
can = Canvas(fenetre,bg='red',height=704 ,width=fenetre.winfo_screenwidth())
can.pack(side=BOTTOM)


#création terrain
t = 1
x_début = 0
y_début = 0
x_fin = 32
y_fin = 32

for i in range (0,48):  
    for j in range (0,22) :
        if t%2 == 1 :
            cc = '#32c258'
        else :
            cc = 'light green'
        t+=1
        carrée = can.create_rectangle(x_début,y_début,x_fin,y_fin,width=1,fill=cc)
        y_début += 32
        y_fin += 32
    
    y_début = 0
    y_fin = 32
    x_début += 32
    x_fin += 32
    t += 1


#génération de pomme au hazard


def mouvement() :
    ...


def play():
    ...




"""p = 864//64
r = 864%64

print(fenetre.winfo_screenwidth())
print(fenetre.winfo_screenheight())
print(p)
print(r)"""




fenetre.mainloop()


