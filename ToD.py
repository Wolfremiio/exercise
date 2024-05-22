from tkinter import *
from tkinter import ttk


class todo:
    def __init__(self, root):
        self.root = root
        self.root.tittle = "To-do-list"
        self.root.geometry("650x410+300+150")

        self.label = Label(
            self.root,
            text="To-Do-List-App",
            font="ariel, 25 bold",
            width=10,
            bd=5,
            bg="#6CAC7F",
            fg="white",
        )
        self.label.pack(side="top", fill=BOTH)

        self.labe2 = Label(
            self.root,
            text="Add Task",
            font="ariel, 18 bold",
            width=10,
            bd=5,
            bg="#6CAC7F",
            fg="white",
        )
        self.labe2.place(x=40, y=54)

        self.labe3 = Label(
            self.root,
            text="Tasks",
            font="ariel, 18 bold",
            width=10,
            bd=5,
            bg="#6CAC7F",
            fg="white",
        )
        self.labe3.place(x=320, y=54)

        # Aquí empezaros como en cuadro de texto donde ingresaremos las tareas, utilizaré el widget de cuadro de texto en tkinter

        self.main_text = Listbox(
            self.root, height=9, bd=3, width=23, font="ariel, 20 italic bold"
        )
        self.main_text.place(x=280, y=100)


def main():
    root = Tk()
    ui = todo(root)
    root.mainloop()


if __name__ == "__main__":

    main()
