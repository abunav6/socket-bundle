def checkValidity(a, n):
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
    return(False)

def isEmpty(x, y, a):
    if(a[x][y] == 0):
        return(True)
    else:
        return(False)

def player_input():
    x, y = input().split()
    x = int(x)
    y = int(y)
    return(x, y)

def printGrid(a):
    for row in a:
        print(row)

def createGrid(n):
    a = []
    for _ in range(n):
        a.append([0]*n)
    return(a)