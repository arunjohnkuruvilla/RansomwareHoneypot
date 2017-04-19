from sys import stdin, stdout
from random import choice
from string import ascii_lowercase



from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
for x in range(1000000):
	s = ''.join([choice(ascii_lowercase) for _ in range(1000000)])
	pdf.cell(40, 10, s)
pdf.output('sample.pdf', 'F')