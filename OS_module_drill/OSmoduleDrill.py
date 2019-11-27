import os
import time



fPath = 'C:\\Users\\ethan\\Documents\\GitHub\\Basic-Python-Projects\\OS_module_drill\\'


def start():
    fileList = os.listdir(fPath)
    
    for fileName in fileList:
        fCon = fileName
        adPath = os.path.join(fPath,fCon)
        if fileName.endswith('.txt'):
            unixTime = os.path.getmtime(adPath)
            modiTime = time.ctime(unixTime)
            print(fileName,modiTime)
    




if __name__ == "__main__":
     start()
