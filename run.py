#! /usr/bin/env python2.7
import ctypes
import sys
import os

import src.monitor as monitor
import src.admin as admin

# Reference:
# msdn.microsoft.com/en-us/library/windows/desktop/bb762153(v=vs.85).aspx

def main():
	if ctypes.windll.shell32.IsUserAnAdmin():
		monitor_object = monitor.Monitor()
		monitor_object.initialize()
	else:
		print os.path.dirname(os.path.abspath(__file__))
		admin_object = admin.Admin()
		admin_object.bootstrap(os.path.abspath(__file__))
		sys.exit(0)

if __name__ == '__main__':
	main()