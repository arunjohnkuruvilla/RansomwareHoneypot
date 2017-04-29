import sys
import os
from random import choice
from string import ascii_lowercase
from pyexcel_xlsx import save_data
from collections import OrderedDict

import config

from fpdf import FPDF

class FS(object):
	def __init__(self):
		self.config = config.configuration

	def generate_random_name(self, extenstion):
		""" Generate random names for files"""
		random_index = ''.join([choice(ascii_lowercase) for _ in range(5)])
		output_location = self.config['package_filesystem_path'] + 'sample' + str(random_index) + extenstion
		return output_location

	def generate_pdf(self, filename=None):
		""" Generate pdf files containing random data."""
		pdf = FPDF()
		pdf.add_page()
		pdf.set_font('Arial', 'B', 16)
		for x in range(2):
			s = ''.join([choice(ascii_lowercase) for _ in range(1000000)])
			pdf.cell(40, 10, s)

		output_location = self.generate_random_name(".pdf")
		pdf.output(output_location, 'F')
		print "[+] File saved to " + output_location
		return

	def generate_xls(self, filename=None):
		""" Generate xlsx files containing random data."""
		return

	def generate_txt(self, filename=None):
		""" Generate txt files containing random data."""
		output_location = self.generate_random_name(".txt")
		output_file = open(output_location, "w")
		for x in xrange(0, 50):
			s = ''.join([choice(ascii_lowercase) for _ in range(1000000)])
			output_file.write(s)
		print "[+] File saved to " + output_location
		return

	def generate_random(self, count=None):
		""" Generate random pdf, xlsx and text files containing random data.
		If a the number of files is not provided, a default number of files are provided. 
		Default number of files is specified in config.py
		"""
		if count:
			for x in xrange(0, count):
				# self.generate_pdf()
				self.generate_xls()
		else:
			for x in xrange(0, self.config['random_file_count']):
				self.generate_pdf()
				# self.generate_xls()
				self.generate_txt()

	def create_dir_tree(self):
		if not os.path.exists(self.config['package_filesystem_path']):
			os.makedirs(self.config['package_filesystem_path'])
		if not os.path.exists(self.config['package_dump_path']):
			os.makedirs(self.config['package_dump_path'])

def main():
	file_system = FS()
	file_system.generate_pdf()

if __name__ == '__main__':
	main()
