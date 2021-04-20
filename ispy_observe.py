import sys
import time
import logging
from watchdog.observers import Observer
#from watchdog.events import LoggingEventHandlier
from watchdog.events import PatternMatchingEventHandler

watchlist = "ispy_watchlist.txt" #name of watchlist file, change once agreed on a file name

observelist = "ispy_directories.txt" #name of file containing the directory names to watch
class Handlers(watchdog.events.PatternMatchingEventHandler):
    def __init__(self): 
         watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=['*.csv'],
                                                             ignore_directories=True, case_sensitive=False)
         logfile = open("logfile.txt", "x")
         logfile.close()

    def on_Created(self, event):
        logfile.open("logfile.txt", "a")
        logfile.write("{0}- was created at {1}".format(events.src_path,  strftime(date.time.now())))
        logfile.close()

    def on_modified(self, event):
        logfile.open("logfile.txt", "a")
        logfile.write("{0}- was modified at {1}".format(events.src_path,  strftime(date.time.now())))

        logfile.close()

    def on_deleted(self, event):
        logfile.open("logfile.txt", "a")
        logfile.write("{0}- was deleted at {1}".format(events.src_path,  strftime(date.time.now())))
        logfile.close()

    def on_moved(self, event):
        logfile.open("logfile.txt", "a")
        logfile.write("{0}- was moved at {1}".format(events.src_path,  strftime(date.time.now())))
        logfile.close()

if __name__ == "__main__":
    #set configuration - change format? user? clientip? process? processname? filename/pathname? 
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    #path to directories containing the files to observe
    with open(observelist, "r") as directories:    
        paths = [line.rstrip('\n') for line in directories]

    #get list of files to monitor
    with open(watchlist, "r") as filelist:
        files = [line.rstrip('\n') for line in filelist]

    #set event handler - do I need to change this to customized?
    event_handler = Handlers(PatternMatchingEventHandler(patterns=files))

    observer = Observer()
    
    #schedule events - should it be recursive?
    for path in paths:    
        observer.schedule(event_handler, path, recursive=False)


    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    finally:
        observer.join()
