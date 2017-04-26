#! /usr/bin/env python2.7

import psutil
import time
import sys
import os
import subprocess
import threading
import re
import admin
import glob
import fnmatch

import config

class Monitor(object):
	# Initialization for Monitor Class
	def __init__(self, regex=None):
		print "initial"
		self.config = config.Config
		print self.config
		self.current_path = os.path.dirname(os.path.realpath(__file__))
		if regex != None:
			self.regex = regex
			self.regex_object = re.compile(self.regex, re.IGNORECASE)
		else:
			self.regex = r".*" + re.escape("sample") + r".*"
			self.regex_object = re.compile(self.regex, re.IGNORECASE)
		return

	# function that monitors files open
	def monitor_processlist(self):
		for proc in psutil.process_iter():
			try:
				pinfo = proc.as_dict(attrs=['pid'])
			except psutil.NoSuchProcess:
				pass
			else:
				try:
					proci = psutil.Process(pinfo['pid'])
					for files in proci.open_files() :
						match = self.regex_object.search(str(files))
						if match is not None:
							print match
							sys.stdout.write('\a')

							print "File being accessed at " + time.ctime() + " by process " + str(pinfo['pid'])
							
							offpid = pinfo['pid']

							randdump = "[" + str(time.time()) + "]dump_" + str(offpid) + ".dmp";

							print "Dumpfile: " + randdump

							dumpcmd = self.config['package_externals_path'] + '\MemoryDD.bat'					
							
							try: 
								#os.system(dumpcmd)
								#subprocess.check_call(dumpcmd, "", stdin=None, stdout=None, stderr=None, shell=False)
								p = subprocess.call([dumpcmd])
								p.communicate()
								
							except Exception as e:
								print e.message
								pass

							while(True):
								for root, dirnames, filenames in os.walk(self.current_path):
									if fnmatch.filter(filenames, '*.img') != []:
										print filename
									#	print filename
									#	# print os.path.join(root, filename)
									
							return True
				except:
					pass
		return False

	def extract_image():
		for root, dirnames, filenames in os.walk(os.path.dirname(os.path.realpath(__file__))):
			for filename in fnmatch.filter(filenames, '*.img'):
				print os.path.join(root, filename)
		return 
	def initialize(self):
		print "monitor initializing"
		while True:
			status = self.monitor_processlist()
			if status == True:
				return	

def main():
	monitor_object = Monitor()
	monitor_object.intialize()

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt as e:
		print e
		print 'Exiting Monitor.'