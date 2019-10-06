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
            print(a)
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
        
        tmp = checkIfWon(grid)
        s.send(str(pos).encode())

        if tmp[0]:
            endGame(s,tmp)
            break

    s.close()

if __name__=="__main__":
    main()
