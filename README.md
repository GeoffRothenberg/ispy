# ispy

ispy is our group's implementation of a file monitoring system. It uses the python library watchdog to monitor for specfic events in specfic files.


# Installation of Python 3 and Watchdog
ispy was written by our group to be run with Python 3. If not already installed, please download at https://www.python.org/downloads/. The minimum recomended version is 3.6.6
We do not preclude usage on Python 2 but we have written it with Python 3 in mind and all features will be available on that version. Our program also requires the library
watchdog. It is available for download freom the Python Package Index here: https://pypi.org/project/watchdog/

# Running the ispy program (after copying this repo of course)
Our project comprises two different programs. The first is ispy_addfile which, as its name suggests, is to add files to be monitored. In order to run this program type `python3 ispy_addfile.py`. The command line will then prompt you to type out filenames to be monitored. Input the relative path of the files you wish to monitor, separated by a comma as instructed.   When done, terminate the program.

The second program is ispy_observe, the monitoring system itself. Like before, type `python3 ispy_observe.py` to run. The program will then execute in that window. In order to modify files and trigger the programs logic you must work in a different terminal. The observers will run until ispy-observe.py is terminated. In order to view the logfile of events simply open the file "ispy_logfile.txt" that will be created automatically by the program. 



# Note:
The program is not able to see WHO has changed a file, only WHAT and HOW it has been changed. This is a limitation inherent in all implementations of watchdog and inotify. For more information on the technical issues involved see the answer on this StackExchange thread: https://stackoverflow.com/questions/47623037/how-would-i-get-the-pid-of-the-process-causing-a-file-system-event
