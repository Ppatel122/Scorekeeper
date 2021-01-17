from tkinter import *
import sys

class Scorekeeper(Tk):
    def __init__(self):
        super().__init__()
        self.Setup("n")

    def Setup(self,loop):

        if loop == "y":
            pass

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

    def Players(self):
        self.start.grid_forget()
        self.exit.grid_forget()
        self.Title.grid_forget()
        self.geometry("420x200")

        self.gamename = Frame(self)
        self.gnameentry = Entry(self.gamename, width = 13)
        self.gnamelabel = Label(self.gamename, text = "What Game are you playing?", font = 15)

        self.players = Frame(self)

        self.p1entry = Entry(self.players, width=10)
        self.p1label = Label(self.players, text="Player 1",padx = 20)

        self.p2entry = Entry(self.players, width=10)
        self.p2label = Label(self.players, text="Player 2", padx = 20)

        self.p3entry = Entry(self.players, width=10)
        self.p3label = Label(self.players, text="Player 3", padx = 20)

        self.p4entry = Entry(self.players, width=10)
        self.p4label = Label(self.players, text="Player 4", padx = 20)

        self.top = Frame(self)
        self.bottom = Frame(self,pady = 10)
        self.instruct = Label(self.top, text = "Enter your names:", font = 15)
        self.contin = Button(self.bottom, text = "Continue", command = self.Start, bg = "green")

        self.top.grid(row = 0, column = 0)
        self.players.grid(row = 1, column = 0)
        self.gamename.grid(row = 2, column = 0)
        self.bottom.grid(row = 3, column = 0)

        self.p1entry.grid(row = 1, column = 0)
        self.p1label.grid(row = 0, column = 0)
        self.p2entry.grid(row = 1, column = 1)
        self.p2label.grid(row = 0, column = 1)
        self.p3entry.grid(row = 1, column = 2)
        self.p3label.grid(row = 0, column = 2)
        self.p4entry.grid(row = 1, column = 3)
        self.p4label.grid(row = 0, column = 3)

        self.gnameentry.grid(row = 0, column = 1)
        self.gnamelabel.grid(row = 0, column = 0)

        self.instruct.grid(row = 0, column = 0)
        self.contin.grid(row = 0, column = 0)

    def Start(self):
        p1 = self.p1entry.get()
        if len(p1) == 0:
            p1 = "Player 1"
        p2 = self.p2entry.get()
        if len(p2) == 0:
            p2 = "Player 2"
        p3 = self.p3entry.get()
        if len(p3) == 0:
            p3 = "Player 3"
        p4 = self.p4entry.get()
        if len(p4) == 0:
            p4 = "Player 4"
        gname = self.gnameentry.get()
        if len(gname) == 0:
            gname = "Game"

        self.top.grid_forget()
        self.players.grid_forget()
        self.gamename.grid_forget()
        self.bottom.grid_forget()
        self.geometry("420x400")

        self.gametitle = Frame(self)
        self.scoreroundtitle = Frame(self)
        self.scoreround = Frame(self)
        self.scoreroundadd = Frame(self)
        self.scoretitle = Frame(self)
        self.scorebox = Frame(self)
        self.endbut = Frame(self)

        self.gametitlelabel = Label(self.gametitle,font = 14, text = gname)
        self.gametitlelabel.grid(row = 0, column = 0)

        self.scoreroundlabel = Label(self.scoreroundtitle, font = 12, text = "Round Score")
        self.scoreroundlabel.grid(row = 0, column = 0)

        self.p1entry = Entry(self.scoreround, width=10)
        self.p1label = Label(self.scoreround, text=p1,padx = 20)
        self.p2entry = Entry(self.scoreround, width=10)
        self.p2label = Label(self.scoreround, text=p2, padx = 20)
        self.p3entry = Entry(self.scoreround, width=10)
        self.p3label = Label(self.scoreround, text=p3, padx = 20)
        self.p4entry = Entry(self.scoreround, width=10)
        self.p4label = Label(self.scoreround, text=p4, padx = 20)
        self.p1entry.grid(row = 1, column = 0)
        self.p1label.grid(row = 0, column = 0)
        self.p2entry.grid(row = 1, column = 1)
        self.p2label.grid(row = 0, column = 1)
        self.p3entry.grid(row = 1, column = 2)
        self.p3label.grid(row = 0, column = 2)
        self.p4entry.grid(row = 1, column = 3)
        self.p4label.grid(row = 0, column = 3)

        self.roundaddbut = Button(self.scoreroundadd, text = "Add Scores", command = self.AddRound, bg = "green")
        self.roundaddbut.grid(row = 0, column = 0)

        self.endbutton = Button(self.endbut, text = "End Game", command = self.Results, bg = "red")
        self.endbutton.grid(row = 0, column = 0, pady = 5)

        self.gametitle.grid(row = 0, column = 0)
        self.scoreroundtitle.grid(row = 1, column = 0)
        self.scoreround.grid(row = 2, column = 0)
        self.scoreroundadd.grid(row = 3, column = 0)
        self.scoretitle.grid(row = 4, column = 0)
        self.scorebox.grid(row = 5, column = 0)
        self.endbut.grid(row = 6, column = 0)

    def Results(self):
        pass

    def AddRound(self):
        pass


if __name__ == "__main__":
    score = Scorekeeper()
    score.mainloop()
