import watchdog.events
import watchdog.observers
import datetime


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
	

