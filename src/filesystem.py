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
		random_index = ''.join([choice(ascii_lowercase) for _ in range(5)])
		output_location = self.config['package_filesystem_path'] + 'sample' + str(random_index) + extenstion
		return output_location

	def generate_pdf(self, filename=None):
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
		'''
		data = OrderedDict() # from collections import OrderedDict
		random_data = []
		random_content = []
		for x in xrange(0, 10000):
			random_content.append(choice(ascii_lowercase))
		for x in xrange(0, 2):
			random_data.append(random_content)

		data.update({"Sheet 1": random_data})

		output_location = self.random_name_generate(".xlsx")
		save_data(output_location, data)
		print "[+] File saved to " + output_location
		'''
		return

	def generate_txt(self, filename=None):
		output_location = self.generate_random_name(".txt")
		output_file = open(output_location, "w")
		for x in xrange(0, 100):
			s = ''.join([choice(ascii_lowercase) for _ in range(1000000)])
			output_file.write(s)
		print "[+] File saved to " + output_location
		return

	def generate_random(self, count=None):
		if count:
			for x in xrange(0, count):
				# self.generate_pdf()
				self.generate_xls()
		else:
			for x in xrange(0, 5):
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
