# -*- coding: utf-8 -*-
"""
    run
    ~~~~~~~~~~~~

    Implements admin priviledge escalation.

    :copyright: (c) 2017 by Arun John Kuruvilla.
"""
import ctypes
import sys
import os

import src.monitor as monitor
import src.admin as admin
import src.config as config

def main():
	config_object = config.Config()
	"""Updates the values in the config from a Python file.
	"""

	if ctypes.windll.shell32.IsUserAnAdmin():
		# If current user has adminstrator privileges
		# Initialize and start monitor object
		print "Current priviledge level is Administrator. Initializing and starting monitor."
		try:
			monitor_object = monitor.Monitor()
			monitor_object.initialize()
		except Exception as e:
			print e.message
	else:
		print "Current priviledge level is not Administrator. Initializing and starting privilege escalation."
		# If current user does not have adminstrator privileges
		current_script = config_object['package_path'] + '\\' + __file__

		# Initialie admin object
		admin_object = admin.Admin()
		admin_object.bootstrap(current_script)
		sys.exit(0)

if __name__ == '__main__':
	main()