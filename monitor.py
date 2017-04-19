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

def monitor(regex):
	
	for proc in psutil.process_iter():
		try:
			pinfo = proc.as_dict(attrs=['pid'])
		except psutil.NoSuchProcess:
			pass
		else:
			try:
				proci = psutil.Process(pinfo['pid'])
				for files in proci.open_files() :
					match = regex.search(str(files))
					if match is not None:

						sys.stdout.write('\a')

						print "File being accessed at " + time.ctime() + " by process " + str(pinfo['pid'])
						
						offpid = pinfo['pid']

						randdump = "[" + str(time.time()) + "]dump_" + str(offpid) + ".dmp";

						print "Dumpfile: " + randdump

						dumpcmd = str(os.path.dirname(os.path.realpath(__file__))) + '\MemoryDD.bat'					
						
						os.system(dumpcmd)

						for root, dirnames, filenames in os.walk(os.path.dirname(os.path.realpath(__file__))):
							print filenames
							for filename in fnmatch.filter(filenames, '*.img'):
								print os.path.join(root, filename)
								
						return True
			except:
				pass
	return False

def main():
	#if not admin.isUserAdmin():
	#	admin.runAsAdmin()
	while True:
		my_regex = r".*" + re.escape("sample") + r".*"
	
		regex = re.compile(my_regex, re.IGNORECASE)

		status = monitor(regex)
		if status == True:
			return	

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt as e:
		print e
		print 'Exiting Monitor.'