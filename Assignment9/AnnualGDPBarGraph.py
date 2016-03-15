"""
Class to plot a bar graph displaying annual GDP per capita by country.

Author: kk3175
Date: 11/24/2015
Class: DSGA 1007, Assignment 9
"""

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from GDPData import GDPData

class AnnualGDPBarGraph:
	annualGDPByCountry = None
	year = None	
	
	# Assumes year argument is valid
	def __init__(self, gdpData, year):
		self.year = year
		self.annualGDPByCountry = gdpData.obtainAnnualGDPByCountry(self.year)
		self.annualGDPByCountry = self.annualGDPByCountry.sort_values(self.year)

	def plotAnnualGDPBarGraph(self):
		plt.close()
		title = ('GDP per capita by Country in Year %s ') % self.year
		self.annualGDPByCountry.plot(kind='bar', title=title, legend=False, fontsize=7.25, color='yellow', alpha=0.3, figsize=(28,28))
		plt.xlabel('Country')
		plt.ylabel('GDP per capita')
		plt.show()
