import os
import shutil

mediapath = ['/storage/emulated/0/Download','/storage/emulated/0/Pictures/reddit_sync','/storage/emulated/0/FalconPro/SavedPics']
filestomove = []


def copyfile(paths):
    for item in paths:
        if 'jpg' in item:
##            print file
            shutil.move(item,'/storage/emulated/0/Pictures/Pics')
        elif 'gif' in item:
            shutil.move(item,'/storage/emulated/0/Pictures/Gif')

def getfileslist(dir):
    fileswithpath = []
    files = os.listdir(dir)
    for item in files:
        fileswithpath.append(dir +'/'+ item)
    return fileswithpath


for item in mediapath:
    filestomove = getfileslist(item)
    copyfile(filestomove)