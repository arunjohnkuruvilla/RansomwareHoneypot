# -*- coding: utf-8 -*-
"""
    filesystem
    ~~~~~~~~~~~~

    Implements filesystem generation functionality.

    :copyright: (c) 2017 by Arun John Kuruvilla.
"""

import sys
import src.filesystem as filesystem

def module_check():
	status = True
	try:
		import fpdf
	except ImportError:
		print "FPDF module not installed."
		status = False
	return status

def help_text():
	return

def generate():
	""" Call the filesystem object to setup the file system
	"""
	file_system = filesystem.FS()
	file_system.create_dir_tree()
	file_system.generate_pdf()
	file_system.generate_xls()
	file_system.generate_txt()

def main():
	if len(sys.argv) < 2:
		print "No command given"
		sys.exit(0);

	if sys.argv[1] == "configure":
		if module_check():
			print "All required modules present."
		else:
			print "Required modules not present."

	elif sys.argv[1] == "generate":
		generate()

	else:
		print "Invalid command given"
		print "usage: setup.py [-h] command"
		print "setup.py: error: too few arguments"

if __name__ == '__main__':
	main()
