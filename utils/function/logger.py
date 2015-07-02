import sys, os, platform

#This function is used to print runtime process and error messages to console and log file
#If the testcase is run on linux, it will only print the runtime process to console and will not create any log files

class Logger(object):
	def __init__(self):
		self.terminal = sys.stdout
		filename = str.split(sys.argv[0],'.') #get scriptname and split by '.' delimiter
		self.log = open("logs/" + filename[0] + '.log' , "w")

	def write(self, message):
		if platform.system() == 'Windows':
			self.terminal.write(message)
			self.log.write(message)
		elif platform.system() == 'Linux':
			self.terminal.write(message)
