import socket
from os import system

from common import *


def main():
    marker = 2
    s = socket.socket()
    port = 3135
    s.connect(('127.0.0.1', port))
    n = int(s.recv(1024).decode())
    grid = create_grid(n)
    print_grid(grid)
    while True:
        a = s.recv(1024).decode()
        try:
            played = int(a)
        except:
            print(a)  # draw or win message
            break
        update_grid(grid, played, 1)  # corresponds to the other player
        system('clear')
        print_grid(grid)

        pos = get_pos(n)

        update_grid(grid, pos, marker)
        print_grid(grid)

        tmp = check_if_won(grid)
        x = end_game(tmp)
        if x[0] and x[-1] == "draw":
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


if __name__ == "__main__":
    main()
