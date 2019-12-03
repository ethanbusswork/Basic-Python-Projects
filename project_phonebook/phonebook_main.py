# Python ver 3.8.0
#
# Author: Ethan Buss
#
# Tested OS: WIN 10 1809
#

import tkinter as tk
from tkinter import *

import phonebook_gui
import phonebook_func


# Fram is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configs
        self.master = master
        self.master.minsize(500,300) # (Height,Width)
        self.master.maxsize(500,300)
        # This CenterWindow method will center the app on the user's screen
        phonebook_func.center_window(self,500,300)
        self.master.title("Tkinter Phonebook")
        self.master.configure(bg="#F0F0F0")
        # This protocol method is a tkinter built in method to search
        # if this user clicks the (X) or close window button on WINDOWS OS
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        # load in the GUI widgets from a separate module,
        # keeping the code compact and organized
        phonebook_gui.load_gui(self)






if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
