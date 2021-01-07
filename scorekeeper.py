import tkinter as tk
from tkinter import *
import sys

def EndGame():
    sys.exit(1)

def Start(players):
    pass

def Players():
    start.place_forget()
    exit.place_forget()
    score.geometry("200x100")
    canvas = tk.Canvas(score, width = 200, height = 100, bg = "gray")
    canvas.pack()

    two = Button(score,text = "2", width = 3,
                  bg="red",command = lambda:  Start(2))
    three = Button(score,text = "3", width = 3,
                   bg="red",command = lambda:  Start(3))
    four = Button(score,text = "4", width = 3,
                  bg="red",command = lambda:  Start(4))
    five = Button(score,text = "5", width = 3,
                  bg="red",command = lambda:  Start(5))
    six = Button(score,text = "6", width = 3,
                 bg="red",command = lambda:  Start(6))

    canvas.create_window(20, 80, window=two)
    canvas.create_window(20, 80, window=three)
    canvas.create_window(20, 80, window=four)
    canvas.create_window(20, 80, window=five)
    canvas.create_window(20, 80, window=six)

    players.mainloop()

if __name__ == "__main__":
    score = tk.Tk()
    score.title("Scorekeeper")
    score.geometry("300x85")
    start = tk.Button(score,text = "New Game", height = 5, width = 20, command
                       = Players, bg = "green")
    start.place(x=0,y=0)
    exit = tk.Button(score,text = "Exit",height = 5, width = 20,command =
                     EndGame, bg = "red")
    exit.place(x=150,y=0)
    score.mainloop()
