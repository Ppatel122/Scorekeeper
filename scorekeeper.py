import tkinter as tk
from tkinter import *
import sys

def EndGame():
    sys.exit(1)

def Start():
    player1.grid_forget()
    player2.grid_forget()
    player3.grid_forget()
    player4.grid_forget()

    instruct.place_forget()
    contin.place_forget()

def Players():
    start.place_forget()
    exit.place_forget()
    score.geometry("420x200")

    player1.grid(row = 0, column = 0, padx = 20, pady = 70)
    player2.grid(row = 0, column = 1, padx = 20, pady = 70)
    player3.grid(row = 0, column = 2, padx = 20, pady = 70)
    player4.grid(row = 0, column = 3, padx = 20, pady = 70)

    p1entry.grid(row = 1, column = 0)
    p1label.grid(row = 0, column = 0)
    p2entry.grid(row = 1, column = 0)
    p2label.grid(row = 0, column = 0)
    p3entry.grid(row = 1, column = 0)
    p3label.grid(row = 0, column = 0)
    p4entry.grid(row = 1, column = 0)
    p4label.grid(row = 0, column = 0)

    instruct.place(x=158,y=16)
    contin.place(x=175,y=150)

if __name__ == "__main__":

    score = tk.Tk()
    score.title("Scorekeeper")
    score.geometry("420x200")

    start = tk.Button(score,text = "New Game", height = 5, width = 20, command
                       = Players, bg = "green")
    exit = tk.Button(score,text = "Exit",height = 5, width = 20,command =
                     EndGame, bg = "red")

    start.place(x=58,y=50)
    exit.place(x=208,y=50)

    player1 = tk.Frame(score)
    p1entry = tk.Entry(player1, width=10)
    p1label = tk.Label(player1, text="Player 1")

    player2 = tk.Frame(score)
    p2entry = tk.Entry(player2, width=10)
    p2label = tk.Label(player2, text="Player 2")

    player3 = tk.Frame(score)
    p3entry = tk.Entry(player3, width=10)
    p3label = tk.Label(player3, text="Player 3")

    player4 = tk.Frame(score)
    p4entry = tk.Entry(player4, width=10)
    p4label = tk.Label(player4, text="Player 4")

    instruct = tk.Label(score, text = "Enter your names")
    contin = tk.Button(score, text = "Continue", command = Start, bg = "green")

    score.mainloop()
