def createTab(length):
    return [[0] * length for i in range(length)]

def calculateNbNeighbour(tab, line, column):
    sum = 0
    for i in range(-1, 2):
        if line + i >= len(tab) or line + i < 0:
            continue
        for j in range(-1, 2):
            if column + j >= len(tab[i]) or column + j < 0:
                continue
            if i != 0 or j != 0:
                sum += tab[line + i][column + j]
    return sum

def lifeOrDeath(tab, line, column, birth, survive, die):
    nbNeighbour = calculateNbNeighbour(tab, line, column)
    if nbNeighbour == birth:
        return 1
    elif nbNeighbour >= die:
        return 0
    elif tab[line][column] == 1 and nbNeighbour == survive:
        return 1
    return 0


def evolution(tab):
    res = createTab(len(tab))
    for i in range(len(tab)):
        for j in range(len(tab)):
            res[i][j] = lifeOrDeath(tab, i, j, 3, 2, 5)
    return res



