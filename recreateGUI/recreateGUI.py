
import tkinter
from tkinter import *

############################################

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(550,200))
        self.master.title('Check files')
        self.master.config(bg='white')

        self.btnBrowse1 = Button(self.master,text='Browse...',width=13,font=("Helvetica", 9),fg='black',bg='white')
        self.btnBrowse1.grid(row=0,column=0,padx=(20,0),pady=(50,0))

        self.btnBrowse2 = Button(self.master,text='Browse...',width=13,font=("Helvetica", 9),fg='black',bg='white')
        self.btnBrowse2.grid(row=1,column=0,padx=(20,0),pady=(10,0))

        self.btnCheckFiles = Button(self.master,text='Check for files...',width=13,height=2,font=("Helvetica", 9),fg='black',bg='white')
        self.btnCheckFiles.grid(row=2,column=0,padx=(20,0),pady=(10,0))

        self.btnClose = Button(self.master,text='Close Program',width=13,height=2,font=("Helvetica", 9),fg='black',bg='white')
        self.btnClose.grid(row=2,column=3,padx=(280,0),pady=(10,0))

        self.entry1 = Entry(self.master,text='',width=45,font=("Helvetica", 11),fg='black',bg='white')
        self.entry1.grid(row=0,column=1,columnspan=3,padx=(30,0),pady=(50,0))
        
        self.entry2 = Entry(self.master,text='',width=45,font=("Helvetica", 11),fg='black',bg='white')
        self.entry2.grid(row=1,column=1,columnspan=3,padx=(30,0),pady=(9,0))



if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
    
