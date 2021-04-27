# iSPY

iSPY is our group's implementation of a file monitoring system. It uses the python library watchdog to monitor for specific events in specific files.


# Installation of Python 3 and Watchdog
iSPY was written by our group to be run with Python 3. Our repo contains a docker file to install the necessary dependencies (watchdog). The dockerfile is configured to automatically put this into its own directory so as not to copy unecesary files to the image. To build the image run `docker build -t ispy https://github.com/GeoffRothenberg/ispy`

# Running the iSPY program
Our project comprises two different programs, designed to run manually. The first is ispy_addfile.py which, as its name suggests, is to add files to be monitored. In order to run this program type `python3 ispy_addfile.py`. The command line will then prompt you to type out filenames to be monitored. Input the relative path or absolute path of the files you wish to monitor, separated by commas as instructed.   When done, hit enter and the program will add the files.

The second program is ispy_observe.py, the monitoring system itself. Like before, type `python3 ispy_observe.py` to run. The program will then execute in that window. In order to modify files and trigger the programs logic you may work in a different terminal or have the program run in the background. The observers will run until ispy-observe.py is terminated. In order to view the logfile of events simply open the file "ispy_logfile.txt" that will be created automatically by the program. Log entries can also be viewed and filtered using typical command line arguments such as cat and grep.



# Note:
The program is not able to see WHO has changed a file, only WHAT and HOW it has been changed. This is a limitation inherent in all implementations of watchdog and inotify. For more information on the technical issues involved see the answer on this StackExchange thread: https://stackoverflow.com/questions/47623037/how-would-i-get-the-pid-of-the-process-causing-a-file-system-event
