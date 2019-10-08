import socket
import sys
from os import system
from common import *

def main():   
    marker = 2
    s = socket.socket()
    port = 3135
    s.connect(('127.0.0.1', port))
    n = int(s.recv(1024).decode())
    grid = createGrid(n)
    printGrid(grid)
    while True:
        a = s.recv(1024).decode()
        try:
            played = int(a)
        except:
            print(a)                    #draw or win message
            break
        updateGrid(grid,played,1)       #corresponds to the other player
        system('clear')
        printGrid(grid)
        while True:
            pos = int(input("Enter box number [1-{}]\n".format(n**2 )))-1
            if pos<=n**2:
                break
            if pos>n**2:
                print("INVALID INPUT")
                
        updateGrid(grid,pos,marker)
        printGrid(grid)
        
        tmp = checkIfWon(grid)
        x = endGame(tmp)
        if x[0] and x[-1]=="draw":
            print("Draw!")
            s.send("Draw!".encode())
            break
        else:
            if x[0]:
                print(x[1])
                s.send(x[1].encode())
                break
            else:
                s.send(str(pos).encode())

    s.close()

if __name__=="__main__":
    main()
