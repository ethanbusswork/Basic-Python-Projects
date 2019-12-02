
import os
import sqlite3

conn = sqlite3.connect('files.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT \
        )")
    conn.commit()
conn.close()

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
fPath = 'C:\\PyProjects\\'

def start():
    
    conn = sqlite3.connect('files.db')
    
    for fileName in fileList:
        if fileName.endswith('.txt'):
            conn = sqlite3.connect('files.db')
            with conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO tbl_files(col_fname) VALUES (?)", \
                            (fileName,))
                conn.commit()
            conn.close()



if __name__ == "__main__":
     start()
