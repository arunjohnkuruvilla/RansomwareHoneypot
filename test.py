import src.config as config

con = config.Config()

class ClassA(object):
	def __init__(self):
		self.config = con
		self.config['package_path'] = "asdf"

class ClassB(object):
	def __init__(self):
		self.config = con
		print self.config['package_path']

A = ClassA()
B = ClassB()