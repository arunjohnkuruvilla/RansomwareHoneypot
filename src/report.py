import config

class Report(object):
	def __init__(self):
		self.config = config.Config()

	def generate_report(self):
		print "[+] Report generated."