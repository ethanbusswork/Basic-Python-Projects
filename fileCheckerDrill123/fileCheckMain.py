from tkinter import filedialog

from tkinter import *

import tkinter as tk

import os

import time

import sqlite3

import shutil
############################################

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format(900,300))
        self.master.title('askdirectory()GUI')
        self.master.config(bg='white')
        
        # Path 1
        self.lbl_directory1 = tk.Label(self.master,text='Path 1:',font=("Helvetica", 11),bg='gray')
        self.lbl_directory1.grid(row=0,column=1,padx=(30,0),pady=(30,0))

        self.lblDisplay1 = tk.Label(self.master,text='',font=("Helvetica", 11),fg='black',bg='gray')
        self.lblDisplay1.grid(row=0,column=2,padx=(0,0),pady=(30,0),sticky=W)
        
        # Path 2
        self.lbl_directory2 = tk.Label(self.master,text='Path 2:',font=("Helvetica", 11),bg='gray')
        self.lbl_directory2.grid(row=1,column=1,padx=(30,0),pady=(30,0))

        self.lblDisplay2 = tk.Label(self.master,text='',font=("Helvetica", 11),fg='black',bg='gray')
        self.lblDisplay2.grid(row=1,column=2,padx=(0,0),pady=(30,0),sticky=W)
        
        # Select button 1
        self.btnSelect1 = tk.Button(self.master,text="Select Path",font=("Helvetica", 11),
                                   width=15,height=2,command=self.SelectFile1)
        self.btnSelect1.grid(row=0,column=0,padx=(30,0),pady=(30,0),sticky=NE)
        
        # Select button 2
        self.btnSelect2 = tk.Button(self.master,text="Select Path",font=("Helvetica", 11),
                                   width=15,height=2,command=self.SelectFile2)
        self.btnSelect2.grid(row=1,column=0,padx=(30,0),pady=(30,0),sticky=NE)

        # Check Files Button
        self.btnCheck = tk.Button(self.master,text='Check for Files',font=("Helvetica", 11),
                                  width=15,height=2,command=self.CheckFiles)
        self.btnCheck.grid(row=2,column=0,padx=(30,0),pady=(30,0),sticky=W)

        

    def SelectFile1(self):        
        self.dirname1 = filedialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
        self.lblDisplay1.config(text='{}'.format(self.dirname1))
       # return self.dirname1

    def SelectFile2(self):        
        self.dirname2 = filedialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
        self.lblDisplay2.config(text='{}'.format(self.dirname2))
        #return self.dirname2

    def CheckFiles(self):
        conn = sqlite3.connect('files.db')
        fileList = os.listdir(self.dirname1)
    
        for fileName in fileList:
            fCon = fileName
            adPath = os.path.join(self.dirname1,fCon)
            if fileName.endswith('.txt'):
                unixTime = os.path.getmtime(adPath)
                modiTime = time.ctime(unixTime)
                conn = sqlite3.connect('files.db')
                with conn:
                    cur = conn.cursor()
                    cur.execute("INSERT INTO tbl_files(col_fileName,col_modiTime) VALUES (?,?)", \
                            (fileName,modiTime))
                    conn.commit()
                conn.close()
                shutil.move(adPath,self.dirname2)
                print(fileName,modiTime)

################################################################# SQL code

conn = sqlite3.connect('files.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileName TEXT, \
        col_modiTime TEXT \
        )")
    conn.commit()
conn.close()

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
    
