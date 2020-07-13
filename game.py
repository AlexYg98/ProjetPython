from tkinter import *
from lib import generateGrid
from algo import evolution

ROWS = 20
COLUMNS = 20

window = Tk()
window.geometry("480x320")
jeu = Frame(window)
controle = Frame(window)

grid = generateGrid(ROWS, COLUMNS)
buttons = generateGrid(ROWS, COLUMNS)

gameStarted = False


def changeValue(row, col):
    grid[row][col] += 1 - 2 * (grid[row][col])
    buttons[row][col].config(bg="black" if grid[row][col] == 1 else "white")
    print(grid)


def generateCase(row, col):
    block: Button = Button(jeu, width=1, height=1, command=lambda: changeValue(row, col),
                           bg="black" if grid[row][col] == 1 else "white")
    buttons[row][col] = block
    block.grid(row=row, column=col)


def initGrid():
    for i in range(0, ROWS):
        for j in range(0, COLUMNS):
            generateCase(i, j)


def update():
    global gameStarted
    global grid
    if gameStarted:
        newGrid = evolution(grid)

        for i in range(0, ROWS):
            for j in range(0, COLUMNS):
                if newGrid[i][j] != grid[i][j]:
                    changeValue(i, j)

        window.after(500, update)


def event(button):
    global gameStarted
    gameStarted = not gameStarted
    if gameStarted:
        window.after(200, update)
        button.config(text="stop")
    else:
        button.config(text="start")


stop = Button(controle, text="start", command=lambda: event(stop))  # ,command=stop
stop.pack(fill=X)

initGrid()
jeu.grid(row=0, column=0, sticky=N + W)
controle.grid(row=0, column=1, sticky=N + W)
window.mainloop()
