# -*- coding: utf-8 -*-
"""
    report
    ~~~~~~~~~~~~

    Implements report generation functions.

    :copyright: (c) 2017 by Arun John Kuruvilla.
"""
import time
import os

import fnmatch

import config

class Report(object):
	def __init__(self):
		self.config = config.Config()

	def generate_report(self):
		file_found_status = False
		file_location = ""
		while(not file_found_status):
			time.sleep(1)
			for root, dirnames, filenames in os.walk(self.config['package_dump_path']):
				for filename in fnmatch.filter(filenames, '*.img'):
					file_location = os.path.join(root, filename)
					file_found_status = True

		print "[+] File image saved to: " + file_location
		print "[+] Report generated."