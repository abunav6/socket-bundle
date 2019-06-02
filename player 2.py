import socket
import sys


def getBox(a,b):
    return 3*(int(a)-1) + int(b)
    
winPos=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
clientPlay=[]

s = socket.socket()
port = 3135
s.connect(('172.16.132.130', port))

noOfMoves=0

while True:
    z=input("Play your move \n")
    s.sendall(z.encode())   
    row,col=s.recv(1024).decode().split(',')
    clientPlay.append(getBox(row,col))
    noOfMoves+=1
    if noOfMoves==4:
        print('DRAW')
        sys.exit(0)
    elif sorted(clientPlay) in winPos:
        print('GAME OVER, SERVER WINS')
        sys.exit(0)
    #print('Row: ',row,"\nCol: ",col)
s.close()
