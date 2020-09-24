from tkinter import *
import algorithms

class user_interface:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.labelUpper = Label(frame, text = "How many uppercase letters: ")
        self.labelUpper.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.entUpper = Entry(frame, width = 22)
        self.entUpper.grid(row = 0, column = 1, padx = 5, pady = 10, sticky = E)

        self.labelLower = Label(frame, text = "How many lowercase letters: ")
        self.labelLower.grid(row = 1, column = 0, padx = 10, pady = 10)
        self.entLower = Entry(frame, width = 22)
        self.entLower.grid(row = 1, column = 1, padx = 5, pady = 10, sticky = E)

        self.labelDigits = Label(frame, text = "How many digits: ")
        self.labelDigits.grid(row = 2, column = 0, padx = 10, pady = 10)
        self.entDigits = Entry(frame, width = 22)
        self.entDigits.grid(row = 2, column = 1, padx = 5, pady = 10, sticky = E)

        self.labelSpecial = Label(frame, text = "How many special characters: ")
        self.labelSpecial.grid(row = 3, column = 0, padx = 10, pady = 10)
        self.entSpecial = Entry(frame, width = 22)
        self.entSpecial.grid(row = 3, column = 1, padx = 5, pady = 10, sticky = E)

        self.execute = Button(frame, text = "Generate Password", command = self.genPassword)
        self.execute.grid(row = 4, column = 0, padx = 5, pady = 10)

        self.entReturn = Entry(frame, width = 30)
        self.entReturn.grid(row = 4, column = 1, padx = 5, pady = 10)

    def genPassword(self):
        arr = []
        arr.append(self.entUpper.get())
        arr.append(self.entLower.get())
        arr.append(self.entDigits.get())
        arr.append(self.entSpecial.get())
        algorithm = algorithms.algorithms(arr)
        password = algorithm.passwordGenerator()
        self.entReturn.delete(0, END)
        self.entReturn.insert(0, password)
