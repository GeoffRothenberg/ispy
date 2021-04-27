# ispy

ispy is our group's implementation of a file monitoring system. It uses the python library watchdog to monitor for specfic events in specfic files.


# Installation of Python 3 and Watchdog
ispy was written by our group to be run with Python 3. Our repo contains a docker file to install the necessary dependencies (watchdog). The dockerfile is configured to automatically put this into its own directory so as not to copy unecesary files to the image. To build the image run `docker build -t ispy https://github.com/GeoffRothenberg/ispy`

# Running the ispy program
Our project comprises two different programs, designed to run manually. The first is ispy_addfile which, as its name suggests, is to add files to be monitored. In order to run this program type `python3 ispy_addfile.py`. The command line will then prompt you to type out filenames to be monitored. Input the relative path of the files you wish to monitor, separated by a comma as instructed.   When done, terminate the program.

The second program is ispy_observe, the monitoring system itself. Like before, type `python3 ispy_observe.py` to run. The program will then execute in that window. In order to modify files and trigger the programs logic you must work in a different terminal. The observers will run until ispy-observe.py is terminated. In order to view the logfile of events simply open the file "ispy_logfile.txt" that will be created automatically by the program. 



# Note:
The program is not able to see WHO has changed a file, only WHAT and HOW it has been changed. This is a limitation inherent in all implementations of watchdog and inotify. For more information on the technical issues involved see the answer on this StackExchange thread: https://stackoverflow.com/questions/47623037/how-would-i-get-the-pid-of-the-process-causing-a-file-system-event
