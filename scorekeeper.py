from tkinter import *
import sys

class Scorekeeper(Tk):
    def __init__(self):
        super().__init__()
        self.Setup("n")

    def Setup(self,loop):

        if loop == "y":
            self.win.grid_forget()
            self.finish.grid_forget()

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
        self.p1 = self.p1entry.get()
        if len(self.p1) == 0:
            self.p1 = "Player 1"
        self.p2 = self.p2entry.get()
        if len(self.p2) == 0:
            self.p2 = "Player 2"
        self.p3 = self.p3entry.get()
        if len(self.p3) == 0:
            self.p3 = "Player 3"
        self.p4 = self.p4entry.get()
        if len(self.p4) == 0:
            self.p4 = "Player 4"
        gname = self.gnameentry.get()
        if len(gname) == 0:
            gname = "Game"

        self.top.grid_forget()
        self.players.grid_forget()
        self.gamename.grid_forget()
        self.bottom.grid_forget()
        self.geometry("420x300")

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
        self.p1label = Label(self.scoreround, text=self.p1,padx = 20)
        self.p2entry = Entry(self.scoreround, width=10)
        self.p2label = Label(self.scoreround, text=self.p2, padx = 20)
        self.p3entry = Entry(self.scoreround, width=10)
        self.p3label = Label(self.scoreround, text=self.p3, padx = 20)
        self.p4entry = Entry(self.scoreround, width=10)
        self.p4label = Label(self.scoreround, text=self.p4, padx = 20)
        self.p1entry.grid(row = 1, column = 0)
        self.p1label.grid(row = 0, column = 0)
        self.p2entry.grid(row = 1, column = 1)
        self.p2label.grid(row = 0, column = 1)
        self.p3entry.grid(row = 1, column = 2)
        self.p3label.grid(row = 0, column = 2)
        self.p4entry.grid(row = 1, column = 3)
        self.p4label.grid(row = 0, column = 3)

        self.roundaddbut = Button(self.scoreroundadd, text = "Add Scores", command = self.AddRound, bg = "green")
        self.roundaddbut.grid(row = 0, column = 0,pady = 15)

        self.scoretotal = Label(self.scoretitle, font = 12, text = "Total Score")
        self.scoretotal.grid(row = 0, column = 0)

        self.p1scores = 0
        self.p2scores = 0
        self.p3scores = 0
        self.p4scores = 0

        self.p1score = Label(self.scorebox, text=self.p1scores,padx = 20)
        self.p1label = Label(self.scorebox, text=self.p1,padx = 20)
        self.p2score = Label(self.scorebox, text=self.p2scores,padx = 20)
        self.p2label = Label(self.scorebox, text=self.p2, padx = 20)
        self.p3score = Label(self.scorebox, text=self.p3scores,padx = 20)
        self.p3label = Label(self.scorebox, text=self.p3, padx = 20)
        self.p4score = Label(self.scorebox, text=self.p4scores,padx = 20)
        self.p4label = Label(self.scorebox, text=self.p4, padx = 20)
        self.p1score.grid(row = 1, column = 0)
        self.p1label.grid(row = 0, column = 0)
        self.p2score.grid(row = 1, column = 1)
        self.p2label.grid(row = 0, column = 1)
        self.p3score.grid(row = 1, column = 2)
        self.p3label.grid(row = 0, column = 2)
        self.p4score.grid(row = 1, column = 3)
        self.p4label.grid(row = 0, column = 3)

        self.endbutton = Button(self.endbut, text = "End Game", command = self.Results, bg = "red")
        self.endbutton.grid(row = 0, column = 0, pady = 15)

        self.gametitle.grid(row = 0, column = 0)
        self.scoreroundtitle.grid(row = 1, column = 0)
        self.scoreround.grid(row = 2, column = 0)
        self.scoreroundadd.grid(row = 3, column = 0)
        self.scoretitle.grid(row = 4, column = 0)
        self.scorebox.grid(row = 5, column = 0)
        self.endbut.grid(row = 6, column = 0)

    def Results(self):
        maxi = max(self.p1scores,self.p2scores,self.p3scores,self.p4scores)
        winners = []
        if maxi == self.p1scores:
            winners.append(self.p1)
        if maxi == self.p2scores:
            winners.append(self.p2)
        if maxi == self.p3scores:
            winners.append(self.p3)
        if maxi == self.p4scores:
            winners.append(self.p4)

        self.gametitle.grid_forget()
        self.scoreroundtitle.grid_forget()
        self.scoreround.grid_forget()
        self.scoreroundadd.grid_forget()
        self.scoretitle.grid_forget()
        self.scorebox.grid_forget()
        self.endbut.grid_forget()
        self.geometry("400x100")

        i = 0
        line = "Winners are "
        while (True):
            line += winners[i]
            i += 1
            if (i == len(winners)):
                break
            elif(i == len(winners) - 1):
                line += " and "
            else:
                line += ", "

        self.win = Frame(self)
        self.finish = Frame(self)

        self.winnames = Label(self.win, text = line)
        self.winnames.grid(row = 0, column = 0)

        self.finishbut = Button(self.finish, text = "Finish", command = lambda: self.Setup("y"), bg = "red")
        self.finishbut.grid(row = 0, column = 0)

        self.win.grid(row = 0, column = 0)
        self.finish.grid(row = 1, column = 0)

    def AddRound(self):
        self.p1scores += int(self.p1entry.get())
        self.p2scores += int(self.p2entry.get())
        self.p3scores += int(self.p3entry.get())
        self.p4scores += int(self.p4entry.get())

        self.p1score = Label(self.scorebox, text=self.p1scores,padx = 20)
        self.p1label = Label(self.scorebox, text=self.p1,padx = 20)
        self.p2score = Label(self.scorebox, text=self.p2scores,padx = 20)
        self.p2label = Label(self.scorebox, text=self.p2, padx = 20)
        self.p3score = Label(self.scorebox, text=self.p3scores,padx = 20)
        self.p3label = Label(self.scorebox, text=self.p3, padx = 20)
        self.p4score = Label(self.scorebox, text=self.p4scores,padx = 20)
        self.p4label = Label(self.scorebox, text=self.p4, padx = 20)
        self.p1score.grid(row = 1, column = 0)
        self.p1label.grid(row = 0, column = 0)
        self.p2score.grid(row = 1, column = 1)
        self.p2label.grid(row = 0, column = 1)
        self.p3score.grid(row = 1, column = 2)
        self.p3label.grid(row = 0, column = 2)
        self.p4score.grid(row = 1, column = 3)
        self.p4label.grid(row = 0, column = 3)


if __name__ == "__main__":
    score = Scorekeeper()
    score.mainloop()
