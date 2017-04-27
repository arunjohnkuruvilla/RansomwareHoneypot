# -*- coding: utf-8 -*-
"""
    report
    ~~~~~~~~~~~~

    Implements report generation functions.

    :copyright: (c) 2017 by Arun John Kuruvilla.
"""
import time
import os

import config

class Report(object):
	def __init__(self):
		self.config = config.Config()

	def generate_report(self):
		while(True):
			time.sleep(1)
			for root, dirnames, filenames in os.walk(self.config['package_dump_path']):
				for filename in fnmatch.filter(filenames, '*.img'):
					print os.path.join(root, filename)
					break
		print "[+] Report generated."