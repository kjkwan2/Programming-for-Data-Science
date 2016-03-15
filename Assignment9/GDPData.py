"""
Class that handles GDP per capita and country/region data.
Loads the data from files.
Creates new dataframes appropriate for visualizations.

Author: kk3175
Date: 11/24/2015
Class: DSGA 1007, Assignment 9
"""

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

class GDPData:
	# Set the locations and tab names of the files used for country and GDP information
	countriesFile = 'countries.csv'
	incomeFile = 'indicator gapminder gdp_per_capita_ppp.xlsx'
	incomeTab = 'Data'

	# Dataframe objects of the GDPData class
	income = None
	countries = None
	
	def __init__(self):
		self.__constructCountries()
		self.__constructIncome()


	# PRIVATE FUNCTIONS

	# Constructs a dataframe with countries listed as the column header and their corresponding
	# region in column 0
	def __constructCountries(self):
		self.countries = pd.read_csv(self.countriesFile, index_col=0)

	# Constructs a dataframe with row headers consisting of each year between 1800-2012
	# (inclusive) and countries in the column headers. The GDP per capita is specified
	# in the values for each year and country combination.
	def __constructIncome(self):
		# Transpose rows and columns
		self.income = pd.read_excel(self.incomeFile, self.incomeTab).transpose()
		# Set the column headers to the country names located in the first row
		self.income.columns = self.income.iloc[0]
		# Drop the first row since they are country names (which we only want as column headers)
		self.income.drop(self.income.head(1).index, inplace=True)


	# PUBLIC FUNCTIONS

	# Takes one year between 1800-2012 (inclusive) as an argument.
	# Returns a dataframe consisting of different countries in the column headers and
	# their corresponding GDP per capita (for the specified year) in row 0.
	def obtainAnnualGDPByCountry(self, year):
		annualGDPByCountry = self.income.loc[[year], :].transpose()
		# Drop any countries that have a missing GDP/capita value				
		annualGDPByCountry.dropna(axis=0, how='any', inplace=True) 

		return annualGDPByCountry

	# Takes one year between 1800-2012 (inclusive) as an argument.
	# Returns a dataframe consisting of the countries, their corresponding regions, and
	# their corresponding GDP per capita (for the specified year).
	def merge_by_year(self, year):
		mergedByYearData = self.obtainAnnualGDPByCountry(year)
		# Update name of column header		
		mergedByYearData.columns = ['GDP per capita in %s' %year]
		# Merge in the region column
		mergedByYearData = pd.concat([mergedByYearData, self.countries], axis=1)
		# Drop any countries that have a missing region value		
		mergedByYearData.dropna(axis=0, how='any', inplace=True) 
		
		return mergedByYearData
	
	# Takes one year between 1800-2012 (inclusive) as an argument.
	# Returns a dataframe consisting GDP per capita by region (for the specified year).
	def obtainAnnualGDPByRegion(self, year):
		annualGDPByRegion = self.merge_by_year(year)
		# Drop the country row index because it is not needed
		annualGDPByRegion = annualGDPByRegion.reset_index(drop=True)
		# Pivot so each region is a separate column
		annualGDPByRegion = annualGDPByRegion.pivot(annualGDPByRegion.index, columns='Region')
		# Drop the first column header because it is not needed
		annualGDPByRegion.columns = annualGDPByRegion.columns.get_level_values(1)
				
		return annualGDPByRegion
