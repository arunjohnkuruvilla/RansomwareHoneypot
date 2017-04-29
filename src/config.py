# -*- coding: utf-8 -*-
"""
    config
    ~~~~~~~~~~~~

    Implements the configuration related objects.

    :copyright: (c) 2017 by Arun John Kuruvilla.
"""
import os
from sys import platform as _platform

class Config(dict):
	"""Works exactly like a dict"""
	def __init__(self):
		""" Set global configuration variables. 
		"""

		# Sets global paths
		if _platform == "linux" or _platform == "linux2":
		   separator = '/'
		elif _platform == "darwin":
		   separator = '/'
		elif _platform == "win32":
			separator = '\\'

		self['separator'] = separator

		self['package_path'] = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
		self['package_src_path'] = os.path.dirname(os.path.realpath(__file__))
		self['package_filesystem_path'] = os.path.expanduser("~") + separator + 'Desktop' + separator + 'filesystem' + separator
		self['package_externals_path'] = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + separator + 'externals' + separator
		self['package_dump_path'] = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + separator + 'memory_dumps' + separator

		# Sets global counts
		self['random_file_count'] = 2

	def from_file(self):
		"""Updates the values in the config from a Python file.
		Yet to be implemented.
		"""
		return

configuration = Config()