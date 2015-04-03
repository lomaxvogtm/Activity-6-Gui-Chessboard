__author__ = 'Madeleine'


import tkinter as tk
def board_squares():
    for row in range(8):
        for column in range(8):
            if (row + column) % 2 == 0:
                board.create_rectangle((100*row+50), (100*column+50), (100*row+150), (100*column+150), fill='white',outline="black")
            else:
                board.create_rectangle((100*row+50), (100*column+50), (100*row+150), (100*column+150), fill='black',outline="black")


root = tk.Tk()
board = tk.Canvas(root, width = 900, height = 900, bg='gray')
board.grid(row=0, column=0)
board_squares()


root.mainloop()