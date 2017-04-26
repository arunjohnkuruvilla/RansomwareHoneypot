import sys
import os
from random import choice
from string import ascii_lowercase

# from fpdf import FPDF

class FS(object):

	def generate_pdf(self):
		'''
		pdf = FPDF()
		pdf.add_page()
		pdf.set_font('Arial', 'B', 16)
		for x in range(2):
			s = ''.join([choice(ascii_lowercase) for _ in range(1000000)])
			pdf.cell(40, 10, s)
		pdf.output('file_system/sample.pdf', 'F')
		'''
		return

	def generate_xls(self):
		return

	def generate_txt(self):
		return

	def generate_dir_tree(self):
		if not os.path.exists("file_system"):
			os.makedirs("file_system")
		if not os.path.exists("memory_dumps"):
			os.makedirs("memory_dumps")

def main():
	file_system = FS()
	file_system.generate_pdf()

if __name__ == '__main__':
	main()
