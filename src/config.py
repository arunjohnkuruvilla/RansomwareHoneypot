class Config(dict):
	def __init__(self):
		self['package_path'] = os.path.dirname(os.path.realpath(__file__))