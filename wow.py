from tkinter import *
import random
import main
import time

window = Tk()
window.geometry("480x320")
window.configure(bg='#3030E2')
jeu = Frame(window)
controle = Frame(window, width=200,height=200)

#Acquire pos
def alterGrid(row,col,grille):
    grille[row][col] += 1 - 2*(grille[row][col])
    initGrid(grille)
    #print(row,col, grille[row][col], grille)

# définition du tableau
def vivantMort(etat,row,col,grille):
    block = Button(jeu,width=15,height=15,command=lambda: alterGrid(row, col,grille))
    if etat == 0:
        block.image = PhotoImage(file="blanc.png")
    elif etat == 1:
        block.image = PhotoImage(file="noir.png")
    block['image'] = block.image
    return block

tableau = [[random.randint(0,1) for i in range(4)] for j in range(4)]



def  initGrid(grille):
    for i, block_row in enumerate(grille):
           for j, block in enumerate(block_row):
               retour = vivantMort(grille[i][j],i,j,tableau)
               retour.grid(row=i, column=j)

def toRun(epoch):
    tab = main.getTab()
    for i in range(epoch):
        tab = main.evolution(tab)
        initGrid(tab)
        time.sleep(1)

#init composant boutton label

label = Label(controle,text="héhé")
label.pack(fill=X)
stop = Button(controle,text="run once", command=toRun(1))#,command=stop
stop.pack(fill=X)
stop = Button(controle,text="run 10 times", command=toRun(10))#,command=stop
stop.pack(fill=X)

#Application

tableau = main.getTab()
initGrid(tableau)
jeu.grid(row=0,column=0,sticky=N+W)
controle.grid(row=0,column=1,sticky=N+W)
#toRun(tableau)
#controle.pack()
window.mainloop()