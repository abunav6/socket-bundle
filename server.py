import socket
from os import system

from common import *


def main():
    """
    AF_INET is to connect to IPv4 type of addresses (AF_INET6 can be used for IPv6)
    SOCK_STREAM specifies TCP
    https://en.wikipedia.org/wiki/Internet_Protocol
    https://en.wikipedia.org/wiki/Transmission_Control_Protocol
    """
    marker = 1

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 3135
    socket.SO_REUSEPORT = True
    s.bind(('0.0.0.0', port))  # binds to a free address

    n = int(input("Enter the grid size\n"))
    grid = create_grid(n)
    print('Socket bound to port ', port)
    s.listen(3)  # Queue up to arg number of requests

    print_grid(grid)
    c, addr = s.accept()  # Establish the connection
    print('Got connection from ', addr)

    c.send(str(n).encode())  # sends byte like object of the data to the connected system

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

            else:  # otherwise, game is not over
                c.send(str(pos).encode())

        a = c.recv(1024).decode()  # the sent message can have a max length of 1024 bytes

        try:
            played = int(a)
        except:
            print(a)
            break

        update_grid(grid, played, 2)

    c.close()


if __name__ == "__main__":
    main()
