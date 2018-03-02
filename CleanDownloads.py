import os
import shutil
import time


#The script moves files from the source location to destination according to file types defined
#assumes that the destination paths and folders are preexisting


#define the folders to be cleaned
source = ['C:\Users\xxxx\Downloads','C:\Users\xxxx\Desktop']

#define the folder location for the files to be moved
jpgpath = 'C:\Users\xxxx\Downloads\_Jpg'
zippath = 'C:\Users\xxxx\Downloads\_Zipfiles'
mediapath = 'C:\Users\xxxx\Downloads\_Media'
docpath = 'C:\Users\xxxx\Downloads\_docs'

#use the above locations for archiving or change if needed.
archivepaths = [jpgpath,zippath,mediapath,docpath]
filestomove = []

# time period to Archive
now = time.time()
week_ago = now - 60*60*24*7

def copyfile(paths):
    for item in paths:
##        print file
        if getdestination(item):
            try:
                shutil.move(item,getdestination(item))
                print "Moved" + str(item)
            except Exception as e:
                print e
                print str(item) + 'failed to move'



def checkcreateddate(item):
    modified_date = os.path.getmtime(item)
    if modified_date < week_ago:
        print str(item) + "is older" + "\n"
        return True
    else:
        print str(item) + "is new" + "\n"
        return False

def getfileslist(dir):
    fileswithpath = []
    files = os.listdir(dir)
    for item in files:
        fileswithpath.append(dir +'/'+ item)
    return fileswithpath

def getdestination(item):
        if '.jpg' in item or '.JPG' in item :
            return jpgpath
        elif '.png' in item:
            return jpgpath
        elif '.docx' in item or '.xlsx' in item or '.doc' in item or '.rtf' in item or '.txt' in item or '.xls' in item:
            return docpath
        elif '.zip' in item :
            return zippath
        elif '.mp4' in item or '.avi' in item or '.flv' in item:
            return mediapath
        else:
            return False

def archivefile(file):
    for item in file:
        if getdestination(item):
            try:
                if checkcreateddate(item):
                    shutil.move(item,getdestination(item)+'\Archive')
                    print str(item) + 'has been archived'
            except Exception as e:
                print e
                print str(item) + 'failed to archive'

#Cleanup items

for item in source:
    filestomove = getfileslist(item)
    copyfile(filestomove)

#Archive items

for item in archivepaths:
    filestomove = getfileslist(item)
    archivefile(filestomove)