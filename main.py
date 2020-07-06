import time

def createTab(length):
    return [[0] * length for i in range(length)]


def displayTab(tab):
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            print(tab[i][j], end='|')
        print()
    print("_________________")


def lifeOrDeath(tab, line, column, birth, survive, die):
    sum = 0
    for i in range(-1, 2):
        if line + i >= len(tab) or line + i < 0:
            continue
        for j in range(-1, 2):
            if column + j >= len(tab[i]) or column + j < 0:
                continue
            if i != 0 or j != 0:
                sum += tab[line + i][column + j]
    if sum == birth:
        return 1
    elif sum >= die:
        return 0
    elif tab[line][column] == 1 and sum == survive:
        return 1
    return 0


def evolution(tab):
    res = createTab(len(tab))
    for i in range(len(tab)):
        for j in range(len(tab)):
            res[i][j] = lifeOrDeath(tab, i, j, birth, survie, die)
    return res


tab = createTab(11)
tab[5][3] = 1
tab[5][4] = 1
tab[5][5] = 1
tab[5][6] = 1
tab[5][7] = 1
birth = 3
survie = 2
die = 5

for i in range(10):
    displayTab(tab)
    tab = evolution(tab)
    time.sleep(0.1)

def getTab():
    return tab