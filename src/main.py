import user_interface
from tkinter import *

if __name__ == "__main__":

    root = Tk()
    calculator = user_interface.user_interface(root)
    root.title("Password Generator")
    root.mainloop()