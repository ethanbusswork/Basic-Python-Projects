from tkinter import filedialog

from tkinter import *

import tkinter as tk
############################################

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(900,200))
        self.master.title('askdirectory()GUI')
        self.master.config(bg='white')

        self.lbl_directory = tk.Label(self.master,text='Directory:',font=("Helvetica", 11),bg='gray')
        self.lbl_directory.grid(row=0,column=0,padx=(30,0),pady=(30,0))

        self.lblDisplay = tk.Label(self.master,text='',font=("Helvetica", 11),fg='black',bg='gray')
        self.lblDisplay.grid(row=0,column=1,padx=(30,0),pady=(30,0))

        self.btnSelect = tk.Button(self.master,text="Select File",font=("Helvetica", 11),width=10,height=2,command=self.SelectFile)
        self.btnSelect.grid(row=2,column=0,padx=(30,0),pady=(30,0),sticky=NE)

    def SelectFile(self):
        dirname = ''
        dirname = filedialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
        self.lblDisplay.config(text='{}'.format(dirname))
        

        

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
    
