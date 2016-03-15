"""
Unit test for the GDP Data class. Tests to make sure that the countries and income
data were loaded properly from their respective csv and xlsx files.

Author: kk3175
Date: 11/24/2015
Class: DSGA 1007, Assignment 9
"""

from unittest import TestCase
import pandas as pd
from GDPData import GDPData

class GDPDataTest(TestCase):
	def test_GDPDataIncomeLoadedCorrectly(self):
		gdpDataTest = GDPData()
		self.assertEquals(gdpDataTest.income.shape, (213, 260))

	def test_GDPDataCountriesLoadedCorrectly(self):
		gdpDataTest = GDPData()
		self.assertEquals(gdpDataTest.countries.shape, (194, 1))
