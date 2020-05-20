##python 2.7
from Tkinter import *


class MainGui(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg="white")
        #parent.attributes("-fullscreen", True)
        self.setupGUI()

    def setupGUI(self):
        self.display = Label(self, text="",
                             anchor=E, bg="white", height=1, width=15, font=("TexGyreAdventor", 45))
        self.display.grid(row=0, column=0, columnspan=4, sticky=N + E + S + W)
        self.pack(fill=BOTH, expand=1)

        # set row and col spacing
        for row in range(7):
            Grid.rowconfigure(self, row, weight=1)
        for column in range(4):
            Grid.columnconfigure(self, row, weight=1)

        # 0 button first row (
        img = PhotoImage(file="images/lpr.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, \
                        activebackground="white", command=lambda: self.process("("))
        button.image = img
        button.grid(row=1, column=0, sticky=N + E + S + W)

        # 1 button 1 row )
        img = PhotoImage(file="images/rpr.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, \
                        activebackground="white", command=lambda: self.process(")"))
        button.image = img
        button.grid(row=1, column=1, sticky=N + E + S + W)

        # 2 button 1 row clr
        img = PhotoImage(file="images/clr.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, \
                        activebackground="white", command=lambda: self.process("clr"))
        button.image = img
        button.grid(row=1, column=2, sticky=N + E + S + W)

        # 3 button 1 row back
        img = PhotoImage(file="images/bak.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, \
                        activebackground="white", command=lambda: self.process("bak"))
        button.image = img
        button.grid(row=1, column=3, sticky=N + E + S + W)
        #################### 2nd row
        # 0 button 2 row 7
        img = PhotoImage(file="images/7.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, \
                        activebackground="white", command=lambda: self.process("7"))
        button.image = img
        button.grid(row=2, column=0, sticky=N + E + S + W)

        # 1 button 2 row 8
        img = PhotoImage(file="images/8.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, \
                        activebackground="white", command=lambda: self.process("8"))
        button.image = img
        button.grid(row=2, column=1, sticky=N + E + S + W)

        # 2 button 2 row 9
        img = PhotoImage(file="images/9.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, \
                        activebackground="white", command=lambda: self.process("9"))
        button.image = img
        button.grid(row=2, column=2, sticky=N + E + S + W)

        # 3 button 2 row /
        img = PhotoImage(file="images/div.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, \
                        activebackground="white", command=lambda: self.process("/"))
        button.image = img
        button.grid(row=2, column=3, sticky=N + E + S + W)

        ##########row3

        # 0 button 3 row 4
        img = PhotoImage(file="images/4.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, \
                        activebackground="white", command=lambda: self.process("4"))
        button.image = img
        button.grid(row=3, column=0, sticky=N + E + S + W)

        # 1 button 3 row 5
        img = PhotoImage(file="images/5.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, \
                        activebackground="white", command=lambda: self.process("5"))
        button.image = img
        button.grid(row=3, column=1, sticky=N + E + S + W)

        # 2 button 3 row 6
        img = PhotoImage(file="images/6.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, \
                        activebackground="white", command=lambda: self.process("6"))
        button.image = img
        button.grid(row=3, column=2, sticky=N + E + S + W)

        # 3 button 3 row *
        img = PhotoImage(file="images/mul.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, \
                        activebackground="white", command=lambda: self.process("*"))
        button.image = img
        button.grid(row=3, column=3, sticky=N + E + S + W)

        ######## row 4
        # 0 button 4 row 1
        img = PhotoImage(file="images/1.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, \
                        activebackground="white", command=lambda: self.process("1"))
        button.image = img
        button.grid(row=4, column=0, sticky=N + E + S + W)

        # 1 button 4 row 2
        img = PhotoImage(file="images/2.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, \
                        activebackground="white", command=lambda: self.process("2"))
        button.image = img
        button.grid(row=4, column=1, sticky=N + E + S + W)

        # 2 button 4 row 3
        img = PhotoImage(file="images/3.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, \
                        activebackground="white", command=lambda: self.process("3"))
        button.image = img
        button.grid(row=4, column=2, sticky=N + E + S + W)

        # 3 button 4 row -
        img = PhotoImage(file="images/sub.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, \
                        activebackground="white", command=lambda: self.process("-"))
        button.image = img
        button.grid(row=4, column=3, sticky=N + E + S + W)

        ##########row5
        # 0 button 5 row 0
        img = PhotoImage(file="images/0.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, \
                        activebackground="white", command=lambda: self.process("0"))
        button.image = img
        button.grid(row=5, column=0, sticky=N + E + S + W)

        # 1 button 5 row .
        img = PhotoImage(file="images/dot.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, \
                        activebackground="white", command=lambda: self.process("."))
        button.image = img
        button.grid(row=5, column=1, sticky=N + E + S + W)

        # 3 button 5 row +
        img = PhotoImage(file="images/add.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, \
                        activebackground="white", command=lambda: self.process("+"))
        button.image = img
        button.grid(row=5, column=3, sticky=N + E + S + W)

        ##########row6
        # 0&1 button 6 row =
        img = PhotoImage(file="images/eql-wide.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, \
                        activebackground="white", command=lambda: self.process("="))
        button.image = img
        button.grid(row=6, column=0, columnspan=2, sticky=N + E + S + W)

        # 2 button 6 row **
        img = PhotoImage(file="images/pow.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, \
                        activebackground="white", command=lambda: self.process("**"))
        button.image = img
        button.grid(row=6, column=2, sticky=N + E + S + W)

        # 3 button 6 row %
        img = PhotoImage(file="images/mod.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, \
                        activebackground="white", command=lambda: self.process("%"))
        button.image = img
        button.grid(row=6, column=3, sticky=N + E + S + W)

    def process(self, button):
        global result  # stores result as a global variable, allowing for checking if a result is displayed
        if button == "clr":
            self.display["text"] = ""
        elif button == "bak":
            self.display["text"] = self.display["text"][0:-1]   # removes right most character in string
        elif button == "=":
            # get everything already on screen, store as expr
            try:
                expr = self.display["text"]
                result = str(eval(expr))
                if len(result) > 14:  # length check for answer, truncate if long
                    result = result[0:11] + "..."
                self.display["text"] = result
            except:
                self.display["text"] = "ERROR"
        else:
            if self.display["text"] == "ERROR" or self.display["text"] == result:  # clear on error/result text
                self.display["text"] = ""
            if len(self.display["text"]) < 14:  # do not allow input if more than 14 chars entered
                self.display["text"] += button


result = None  # initializes result variable
##
# make window
window1 = Tk()
window1.title("cal q later")

# make gui
zz = MainGui(window1)

window1.mainloop()
