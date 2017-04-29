# -*- coding: utf-8 -*-
"""
    setup
    ~~~~~~~~~~~~

    Implements basic installation and setup of filesystem.

    :copyright: (c) 2017 by Arun John Kuruvilla.
"""

import sys

import src.filesystem as filesystem

def module_check():
	""" Checks whether required modules are installed
	"""
	status = True
	try:
		import fpdf
		import enum
		import psutil
	except ImportError as e:
		status = False
		if "fpdf" in repr(e):
			print "[-] FPDF module not installed. Run the following commands:"
			print "[-] python -m pip install fpdf"
		if "enum" in repr(e):
			print "[-] Enum module not installed. Run the following commands:"
			print "[-] python -m pip install enum34"
		if "psutil" in repr(e):
			print "Enum module not installed. Run the following commands:"
			print "python -m pip install psutil"

	return status

def help_text():
	""" Prints general help text
	"""
	return

def generate():
	""" Call the filesystem object to setup the file system
	"""
	file_system = filesystem.FS()
	file_system.create_dir_tree()
	file_system.generate_random()

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
