from tkinter import *
import sys

class Scorekeeper(Tk):
    def __init__(self):
        super().__init__()
        self.title("Scorekeeper")
        self.geometry("200x200")

        self.Title = Label(self, text = "Scorekeeper", font = 25)
        self.start = Button(self,text = "New Game", height = 2, width = 10,
                          command = self.Players, bg = "green")
        self.exit = Button(self,text = "Exit",height = 1, width = 7,command =
                         self.EndGame, bg = "red")

        self.Title.grid(row = 0, column = 0)
        self.start.grid(row = 1, column = 0)
        self.exit.grid(row = 2, column = 0)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def EndGame(self):
        sys.exit(1)

    def Start(self):
        self.player1.grid_forget()
        self.player2.grid_forget()
        self.player3.grid_forget()
        self.player4.grid_forget()

        self.instruct.place_forget()
        self.contin.place_forget()

        self.endbut = Button(self, text = "End Game", command = self.Results, bg = "red")

    def Players(self):
        self.start.grid_forget()
        self.exit.grid_forget()
        self.Title.grid_forget()
        self.geometry("420x200")

        self.player1 = Frame(self)
        self.p1entry = Entry(self.player1, width=10)
        self.p1label = Label(self.player1, text="Player 1", font = 15)

        self.player2 = Frame(self)
        self.p2entry = Entry(self.player2, width=10)
        self.p2label = Label(self.player2, text="Player 2",font = 15)

        self.player3 = Frame(self)
        self.p3entry = Entry(self.player3, width=10)
        self.p3label = Label(self.player3, text="Player 3", font = 15)

        self.player4 = Frame(self)
        self.p4entry = Entry(self.player4, width=10)
        self.p4label = Label(self.player4, text="Player 4", font = 15)

        self.instruct = Label(self, text = "Enter your names", font = 20)
        self.contin = Button(self, text = "Continue", command = self.Start, bg = "green")

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

        self.instruct.place(x=144,y=16)
        self.contin.place(x=184,y=150)

    def Results(self):
        pass

    def AddRound(self):
        pass


if __name__ == "__main__":
    score = Scorekeeper()
    score.mainloop()
