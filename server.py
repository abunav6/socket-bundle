import socket
from os import system

from common import *


def main():
    marker = 1
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 3135
    socket.SO_REUSEPORT = True
    s.bind(('0.0.0.0', port))

    n = int(input("Enter the grid size\n"))
    grid = create_grid(n)
    print('Socket bound to port ', port)
    s.listen(3)

    print_grid(grid)
    c, addr = s.accept()
    print('Got connection from ', addr)

    c.send(str(n).encode())
    while True:
        system('clear')
        print_grid(grid)

        pos = get_pos(n)

        update_grid(grid, pos, marker)
        print_grid(grid)

        tmp = check_if_won(grid)

        e = end_game(tmp)
        if e[0] and e[-1] == "draw":
            print("Draw!")
            c.send("Draw!".encode())
            break

        else:
            if e[0]:
                print(e[1])  # win message
                c.send(e[1].encode())
                break
            # otherwise, game is not over
            else:
                c.send(str(pos).encode())

        a = c.recv(1024).decode()

        try:
            played = int(a)
        except:
            print(a)
            break

        update_grid(grid, played, 2)

    c.close()


if __name__ == "__main__":
    main()
