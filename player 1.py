import socket
import sys
from os import system

from common import *


def main():
    marker = 1
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 3135
    try:
        s.bind(('0.0.0.0', port))
    except OSError:
        port+=1
        s.bind(('0.0.0.0', port))
    
    
    n = int(input("Enter the grid size\n"))
    grid = createGrid(n)
    print ('Socket bound to port ',port)
    s.listen(3)

    printGrid(grid)
    c, addr = s.accept()
    print ('Got connection from ', addr)

    c.send(str(n).encode())
    while True:
        system('clear')
        printGrid(grid)
        #get the position
        while True:
            pos = int(input("Enter box number [1-{}]\n".format(n**2 )))-1
            if pos<=n**2:
                break
            if pos>n**2:
                print("INVALID INPUT")
        
        updateGrid(grid,pos,marker)
        printGrid(grid)
        
        tmp = checkIfWon(grid)    
        c.send(str(pos).encode())
        
        
        if tmp[0]:
            endGame(c,tmp)
            break
            

        a = c.recv(1024).decode()
        print(a)
        try:
            played = int(a)
        except:
            print(a)
            break
        
        updateGrid(grid,played,2)
    

    c.close()
    
if __name__=="__main__":
    main()