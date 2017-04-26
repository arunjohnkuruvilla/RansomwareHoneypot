# -*- coding: utf-8 -*-
"""
    config
    ~~~~~~~~~~~~

    Implements the configuration related objects.

    :copyright: (c) 2017 by Arun John Kuruvilla.
"""
import os

class Config(dict):
	"""Works exactly like a dict"""
	def __init__(self):
		self['package_path'] = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
		self['package_src_path'] = os.path.dirname(os.path.realpath(__file__))
		self['package_externals_path'] = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + '\externals'

	def from_file(self):
		"""Updates the values in the config from a Python file."""
		return
