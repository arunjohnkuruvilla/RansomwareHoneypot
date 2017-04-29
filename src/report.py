# -*- coding: utf-8 -*-
"""
    report
    ~~~~~~~~~~~~

    Implements report generation functions.

    :copyright: (c) 2017 by Arun John Kuruvilla.
"""
import time
import os
import hashlib

import fnmatch

import config

class Report(object):

	def __init__(self):
		self.config = config.configuration

	def md5(self, fname):
	    hash_md5 = hashlib.md5()
	    with open(fname, "rb") as f:
	        for chunk in iter(lambda: f.read(4096), b""):
	            hash_md5.update(chunk)
	    return hash_md5.hexdigest()

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

		report_location = self.config['package_path'] + self.config['separator'] + "report.txt"
		report_file = open(report_location, "w")

		report_file.write("DIGITAL FORENSICS FINAL PROJECT \n")
		report_file.write("REPORT\n")
		report_file.write("Arun John Kuruvilla\n")
		report_file.write("N12322107 - ajk665@nyu.edu\n")

		report_file.write("Image Location" + file_location + '\n')
		report_file.write("Image Hash: " + md5(file_location) + '\n') 
		report_file.write("Report Location" + report_location + '\n')

		print "[+] Report saved to: " + report_location

	def generate_text_report(self):
		return