"""
Class for creating histograms and boxplots to visualize GDP per capita by region.

Author: kk3175
Date: 11/24/2015
Class: DSGA 1007, Assignment 9
"""

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from GDPData import GDPData


class VisualAnalysisTools:
	# Class attributes
	year = None
	annualGDPByRegion = None
	regions = None
	boxPlotData = None

	def __init__(self, gdpData, year):
		self.year = year
		self.annualGDPByRegion = gdpData.merge_by_year(self.year)
		self.regions = pd.unique(self.annualGDPByRegion.Region)
		self.boxPlotData = gdpData.obtainAnnualGDPByRegion(self.year)

	# Saves histograms and box plots to individual pdf files.
	def saveGraphs(self):
		self.__saveHistograms()
		self.__saveBoxPlots()
		
	# Helper function to save histograms to a pdf file.
	# Adapted from arjenve from http://stackoverflow.com/questions/11328958/matplotlib-pyplot-save-the-plots-into-a-pdf
	def __saveHistograms(self):
		pdfOutput = PdfPages('histogramsByRegion_Year%s.pdf' %self.year)
		
		# Generates and saves a histogram for each region
		for region in self.regions:
			annualGDPforRegion = self.annualGDPByRegion[self.annualGDPByRegion['Region']==region]
			histogram = self.__plotHistogram(annualGDPforRegion, region)
			pdfOutput.savefig(histogram)
		pdfOutput.close()
		plt.close('all')

	# Helper function that generates and returns a histogram
	def __plotHistogram(self, annualGDPforRegion, region):
		histogram = plt.figure()
		annualGDPforRegion['GDP per capita in %s' % self.year].hist(bins=10)
		plt.title('Distribution of GDP per capita in %s for %s' % (self.year, region))
		plt.ylabel('Number of Countries')
		plt.xlabel('GDP per capita')

		return histogram

	# Helper function that generates and saves a boxplot.	
	def __saveBoxPlots(self):
		self.boxPlotData.plot(kind='box', figsize=(16, 16))
		plt.title('GDP per Capita by Region in Year %s' %self.year)
		plt.ylabel('GDP per Capita')
		plt.xlabel('Region')
		plt.xticks(rotation = -60)
		plt.savefig('boxPlotByRegion_Year%s.pdf' %self.year)
		plt.close('all')
