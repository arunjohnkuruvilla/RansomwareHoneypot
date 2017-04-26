import os

class Config(dict):
	def __init__(self):
		self['package_path'] = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
		self['package_src_path'] = os.path.dirname(os.path.realpath(__file__))
		self['package_externals_path'] = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + '\externals'

	def __getitem__(self, key):
		return self[key]