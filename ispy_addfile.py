#!/usr/bin/env python3

#iSPY
#add filenames to list of files to be watched

import os.path
from os import path

def main():
    watchlist = "ispy_watchlist.txt" #name of watchlist file, specific files to be monitored

    #get list of current files being watched
    filelist = open(watchlist, "r")
    currentlist = filelist.read()
    filelist.close()
    files = []

    #user inputs additional files to watch
    newfiles = input("Enter list of files separated by commas to add to watchlist:\n").split(',')
    for i in range(len(newfiles)):
        newfiles[i]=newfiles[i].strip()

    for i in newfiles:

        #check that file exists
        if(not path.exists(i)):
            print(i + " can not be found\n")
            continue

        #get absolute path of file
        filepath = path.abspath(i)

        #check that file isn't already being watched
        if(filepath+'\n' in currentlist):
            print(filepath + " is already being watched\n")
            continue

        #check that file isn't already in list
        if(filepath+'\n' in files):
            print(filepath+" is already in the list\n")
            continue

	#add file to list
        files.append(filepath+'\n')

    #append list of files
    filelist = open(watchlist, "a")
    filelist.writelines(files)
    filelist.close()

main()
