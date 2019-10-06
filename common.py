def updateGrid(grid,pos,m):
    grid[pos//len(grid)][pos%len(grid)] = m

def createGrid(n):
    
    a = []
    for _ in range(n):
        a.append([0]*n)
    return(a)

def printGrid(arr):
    for _ in arr:
        print(_)
    pass


def endGame(t,tmp):
    a= "Player {} WON!".format(tmp[-1])
    print(a)
    t.send(a.encode())
    


def checkIfWon(a):
    n = len(a)
    # Check rows
    for i in range(n):
        prod = 1       
        for j in range(n):
            prod = prod*a[i][j]       
        if(prod == 8):
            return(True, 2)
        elif(prod == 1):
            return(True, 1)

    # Check columns
    for i in range(n):
        prod = 1       
        for j in range(n):
            prod = prod*a[j][i]       
        if(prod == 8):
            return(True, 2)
        elif(prod == 1):
            return(True, 1)
    
    # Check leading diagonal
    prod = 1
    for i in range(n):
        prod = prod*a[i][i]

    if(prod == 8):
        return(True, 2)
    elif(prod == 1):
        return(True, 1)
    
    # Check non leading diagonal
    prod = 1
    for i in range(n):
        prod = prod*a[i][n-1-i]
    if(prod == 8):
        return(True, 2)
    elif(prod == 1):
        return(True, 1)
    
    # If neither of the players has won the game, continue the game
    return (False,0)