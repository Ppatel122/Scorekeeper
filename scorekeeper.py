from tkinter import *
import sys

class Scorekeeper(Tk):
    def __init__(self):
        super().__init__()
        self.title("Scorekeeper")
        self.geometry("420x200")

        self.start = Button(self,text = "New Game", height = 5, width = 20,
                          command = self.Players, bg = "green")
        self.exit = Button(self,text = "Exit",height = 5, width = 20,command =
                         self.EndGame, bg = "red")

        self.start.place(x=58,y=50)
        self.exit.place(x=208,y=50)

    def EndGame(self):
        sys.exit(1)

    def Start(self):
        self.player1.grid_forget()
        self.player2.grid_forget()
        self.player3.grid_forget()
        self.player4.grid_forget()

        self.instruct.place_forget()
        self.contin.place_forget()

    def Players(self):

        self.player1 = Frame(self)
        self.p1entry = Entry(self.player1, width=10)
        self.p1label = Label(self.player1, text="Player 1")

        self.player2 = Frame(self)
        self.p2entry = Entry(self.player2, width=10)
        self.p2label = Label(self.player2, text="Player 2")

        self.player3 = Frame(self)
        self.p3entry = Entry(self.player3, width=10)
        self.p3label = Label(self.player3, text="Player 3")

        self.player4 = Frame(self)
        self.p4entry = Entry(self.player4, width=10)
        self.p4label = Label(self.player4, text="Player 4")

        self.instruct = Label(self, text = "Enter your names")
        self.contin = Button(self, text = "Continue", command = self.Start, bg = "green")

        self.start.place_forget()
        self.exit.place_forget()
        self.geometry("420x200")

        self.player1.grid(row = 0, column = 0, padx = 20, pady = 70)
        self.player2.grid(row = 0, column = 1, padx = 20, pady = 70)
        self.player3.grid(row = 0, column = 2, padx = 20, pady = 70)
        self.player4.grid(row = 0, column = 3, padx = 20, pady = 70)

        self.p1entry.grid(row = 1, column = 0)
        self.p1label.grid(row = 0, column = 0)
        self.p2entry.grid(row = 1, column = 0)
        self.p2label.grid(row = 0, column = 0)
        self.p3entry.grid(row = 1, column = 0)
        self.p3label.grid(row = 0, column = 0)
        self.p4entry.grid(row = 1, column = 0)
        self.p4label.grid(row = 0, column = 0)

        self.instruct.place(x=158,y=16)
        self.contin.place(x=175,y=150)

if __name__ == "__main__":

    score = Scorekeeper()
    score.mainloop()
