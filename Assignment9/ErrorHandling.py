"""
Error handling class

Author: kk3175
Date: 11/24/2015
Class: DSGA 1007, Assignment 9
"""

class YearRangeError(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)
