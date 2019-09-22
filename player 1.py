import socket
import sys


def createGrid():
    n = int(input("Enter the grid size\n"))
    a = []
    for _ in range(n):
        a.append([0]*n)
    return(a)

def getBox(a,b):
    return 3*(int(a)-1) + int(b)

def printGrid(arr):
    for _ in arr:
        print(_)
    pass

def main():
    winPos=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    serverPlay=[]

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 3135
    try:
        s.bind(('0.0.0.0', port))
    except OSError:
        port+=1
        s.bind(('0.0.0.0', port))
    
    grid = createGrid()

    print ('Socket bound to port ',port)
    s.listen(3)
    print ('socket is listening')
    
    
    printGrid(grid)
    noOfMoves=0
    while True:
        c, addr = s.accept()
        print ('Got connection from ', addr)
        while True:
            try:
                row,col=c.recv(1024).decode().split(',')
            except ValueError as err:
                sys.exit(0)
            serverPlay.append(getBox(row,col))
            noOfMoves+=1
            if noOfMoves==4:
                print('DRAW')
                sys.exit(0)
            elif sorted(serverPlay) in winPos:
                print('GAME OVER, CLIENT WINS')
                sys.exit(0)

            k=input("Play your move \n")
            c.sendall(k.encode())
        c.close()

if __name__=="__main__":
    main()