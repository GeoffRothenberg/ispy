import sys
import time
import logging
from watchdog.observers import Observer
#from watchdog.events import LoggingEventHandlier
from watchdog.events import PatternMatchingEventHandler

watchlist = "ispy_watchlist.txt" #name of watchlist file, change once agreed on a file name

observelist = "ispy_directories.txt" #name of file containing the directory names to watch

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
    event_handler = PatternMatchingEventHandler(patterns=files)

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
