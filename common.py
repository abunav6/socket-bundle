def updateGrid(grid,pos,m):
    if grid[pos//len(grid)][pos%len(grid)]==0:
        grid[pos//len(grid)][pos%len(grid)]= m
    else:
        while True:
            tmp = int(input("Enter a different position!\n"))
            if grid[tmp//len(grid)][tmp%len(grid)] == 0:
                grid[tmp//len(grid)][tmp%len(grid)] = m
                break

def createGrid(n):
    
    a = []
    for _ in range(n):
        a.append([0]*n)
    return(a)

def printGrid(arr):
    for _ in arr:
        print(_)
    pass


def endGame(tmp):
    if tmp[0]:
        a= "Player {} WON!".format(tmp[-1])
        return (True,a)
    elif not tmp[0] and tmp[1]=="draw":
        return (True,"draw")
    else:
        return (False,0)
    

    

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
    
    #check if draw
    for k in a:
        flag = False        #flag = False implies no zeroes
        for b in k:
            if b==0:
                flag = True
                break
        if flag:
            break
    
    if not flag:
        return (False,"draw")
    else:
        return (False,0)    #Game is not over yet