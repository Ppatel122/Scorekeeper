import tkinter as tk
import classes
import sys

def EndGame():
    sys.exit(1)

def main():
    status = "initial"
    if status == "initial":
        score = tk.Tk()
        score.geometry("300x300")
        start = tk.Button(score,text = "New Game")
        start.place(x=0,y=0)
        exit = tk.Button(score,text = "Exit",command = EndGame)
        exit.place(x=65,y=0)
        score.mainloop()
    elif status == "game":
        pass


if __name__ == "__main__":
    main()
