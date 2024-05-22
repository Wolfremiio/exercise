from tkinter import *
from tkinter import ttk


class todo:
    def __init__(self, root):
        self.root = root
        self.root.tittle = "To-do-list"
        self.root.geometry("650x410+300+150")

        self.label = Label(self.root, text="To-Do-List-App", 
        font="ariel, 25 bold", width= 10, bd=5,bg= '#6CAC7F', fg = 'black' )


def main():
    root = Tk()
    ui = todo(root)
    root.mainloop()


if __name__ == "__main__":

    main()
