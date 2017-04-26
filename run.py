#! /usr/bin/env python2.7
import ctypes
import sys
import os

sys.path.append('src')
import monitor as monitor
import admin as admin

# Reference:
# msdn.microsoft.com/en-us/library/windows/desktop/bb762153(v=vs.85).aspx

def main():
	if ctypes.windll.shell32.IsUserAnAdmin():
		monitor_object = monitor.Monitor()
		monitor_object.initialize()
	else:
		admin.bootstrap(sys.argv[0])
		sys.exit(0)

if __name__ == '__main__':
	main()