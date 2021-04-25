import sys
import time
import os

from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler

#Event Handler class
class Handlers(FileSystemEventHandler):
    #Initializing Handler object, creating the logfile
    def __init__(self): 

         logfile = open("ispy_logfile.txt", "a")
         logfile.close()

    #Method to log a file creation event
    def on_created(self, event):
        logfile = open("ispy_logfile.txt", "a")
        logfile.write("\n{0}- was created at {1}".format(event.src_path,  str(time.ctime(time.time()))))
        logfile.close()

    #Method to log a file modification event
    def on_modified(self, event):
        logfile = open("ispy_logfile.txt", "a")
        logfile.write("\n{0}- was modified at {1}".format(event.src_path,  str(time.ctime(time.time()))))
        logfile.close()
      

    #Method to log a file deletion event
    def on_deleted(self, event):
        #if file was actually deleted
        if(not os.path.exists(event.src_path)):
            logfile = open("ispy_logfile.txt", "a")
            logfile.write("\n{0}- was deleted at {1}".format(event.src_path,  str(time.ctime(time.time()))))
            logfile.close()
        #if file was edited by vim
        else:
            logfile = open("ispy_logfile.txt", "a")
            logfile.write("\n{0}- was modified at {1}".format(event.src_path, str(time.ctime(time.time()))))
            logfile.close()

    #Method to log a file relocation event
    def on_moved(self, event):
        logfile = open("ispy_logfile.txt", "a")
        logfile.write("\n{0}- was moved at {1}".format(event.src_path,  str(time.ctime(time.time()))))
        logfile.close()


if __name__ == "__main__":

    watchlist = "ispy_watchlist.txt" #file containing list of files to watch
    observelist = "ispy_directories.txt" #file contaning list of directories to observe     

    #get list of directories to observe
    with open(observelist, "r") as directories:    
        paths = [line.rstrip('\n') for line in directories]

    #get list of files to monitor
    with open(watchlist, "r") as filelist:
        files = [line.rstrip('\n') for line in filelist]

    #set event handler
    event_handler = Handlers()

    observer = Observer()
    
    #schedule events for each directory
    for file in files:    
        observer.schedule(event_handler, file, recursive=False)

    #start the observer
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    finally:
        observer.join()
