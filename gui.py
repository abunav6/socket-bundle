from tkinter import *


def pressed(r, c, size):
    print(f"{size * r + c + 1} was pressed!")


def main(size):
    root = Tk()
    buttons = [Button() for _ in range(size**2)]
    for i in range(size):
        for j in range(size):
            buttons[i][j] = Button(command=lambda a=i,b=j, c=size: pressed(a, b, c), text="")
            buttons[i][j].config(text="1")
            buttons[i][j].grid(row=i, column=j)
    window_width = root.winfo_reqwidth()
    window_height = root.winfo_reqheight()
    position_right = int(root.winfo_screenwidth() / 2 - window_width / 2)
    position_down = int(root.winfo_screenheight() / 2 - window_height / 2)

    root.geometry(f"+{position_right}+{position_down}")
    root.mainloop()


if __name__ == '__main__':
    n = int(input("Enter the grid size: \n"))
    main(n)
