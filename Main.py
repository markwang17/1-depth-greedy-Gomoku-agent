import multiprocessing
from tkinter import *
from Chess import *


def main():
    tk = Tk()
    tk.title("GOMOKU")

    def play():
        multiprocessing.Process(target=start_one_game).start()

    Button(tk, text="Start One Game", fg="black", width=30,
           command=lambda: play()).pack()
    tk.mainloop()


if __name__ == '__main__':
    main()
