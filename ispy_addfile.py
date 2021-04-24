#!/usr/bin/env python3

#iSPY
#add filenames to list of files to be watched

import os.path
from os import path

def main():
    watchlist = "ispy_watchlist.txt" #name of watchlist file, specific files to be monitored
    observelist = "ispy_directories.txt" #name of file containing directories to observe

    #get list of current files being watched
    filelist = open(watchlist, "r")
    currentlist = filelist.read()
    filelist.close()
    files = []

    #get list of current directories being observed
    directories = open(observelist, "r")
    currentdir = directories.read()
    directories.close()
    directories = []

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

	#get file directory
        dir = path.dirname(filepath)

	#check that file directory isn't already being observed
        if(dir+'\n' in currentdir):
            continue

	#check that file directory isn't already in list
        if(dir+'\n' in directories):
            continue

	#add directory to list
        directories.append(dir+'\n')

    #append list of files
    filelist = open(watchlist, "a")
    filelist.writelines(files)
    filelist.close()

    #append list of directories
    directorylist = open(observelist, "a")
    directorylist.writelines(directories)
    filelist.close()

main()
