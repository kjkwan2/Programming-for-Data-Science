"""
Main program for running the three results/output components of Assignment 9:
(1) The head of the countries data set should be shown when loaded.
(2) Display a bar graph of annual GDP per capita by country. Allow the user to select the year.
(3) Generate histograms and boxplots of GDP per capita by region for the years 2007-2012. Save the histograms and boxplots to individual files. Write a short description of the changes observed over this time period in results.txt.

Author: kk3175
Date: 11/24/2015
Class: DSGA 1007, Assignment 9
"""

import pandas as pd
from GDPData import GDPData
from VisualAnalysisTools import VisualAnalysisTools
from AnnualGDPBarGraph import AnnualGDPBarGraph
from ErrorHandling import YearRangeError
import matplotlib
import matplotlib.pyplot as plt


# Asks the user for a year input.
# Validates the user's year input and returns the year if it is valid. 
# If the year input is invalid, appropriate errors are raised.
# Returns -1 if the user is finished.
# Continues this process until the user types 'finish'.
def obtainUserInputYear():
	print '\nThe following graph will display the annual GDP per capita by country for a selected year.'
	print 'Enter a year from 1800-2012, or type \'finish\' to quit.'

	while True:
		try:
			userInputYear = raw_input('Please enter a year from 1800-2012: ')

			if userInputYear == 'finish':
				return -1
			
			# If the year input is not an integer, an error is raised.
			year = int(userInputYear)
		
			# If the year input is not between 1800-2012, an error is raised.
			if isValidYearRange(year):
				return year			
			else:
				raise YearRangeError('The year must be between 1800-2012. Try again.')
			
		except ValueError:
			print 'A year consists of all numbers! Try again.'
		except YearRangeError as error:
			print error.value

# Helper function to check if the year entered by the user is between the specified
# minimum and maximum year range.	
def isValidYearRange(year):
	minYear = 1800
	maxYear = 2012	

	if (year >= minYear) and (year <= maxYear):
		return True
	else:
		return False


def main():
	try:
		gdpData = GDPData()

		# Question 3: Show the head of the countries data set
		print 'Question 3: Head of the countries data set:'	
		print gdpData.income.head(5)

		# Questions 4 and 7: Graphically display the distribution of income per person given 
		# a user input year
		print ('\nQuestion 7: Graph of annual GDP per capita by country.')	

		year = obtainUserInputYear()
		# If the year is -1, the user typed 'finish' and wants to exit this program.
		while year != -1:	
			annualGDPbyCountry = AnnualGDPBarGraph(gdpData, year)
			annualGDPbyCountry.plotAnnualGDPBarGraph()
			year = obtainUserInputYear()
		print 'Onto question 8!'
	
		# Questions 6, 8, and 9: Provide a class that uses exploratory data analysis tools to
		# graphically explore the distribution of income per person by region. 
		# Generate and save the graphs to individual files for the years 2007-2012. 
		# Write a short description of the changes observed over the period in results.txt.
		print ('\nQuestion 8: Visual analysis tools for annual GDP per capita by region are being generated for the years 2007-2012.')	
		years = [2007, 2008, 2009, 2010, 2011, 2012]
		for year in years:
			visualAnalysisTools = VisualAnalysisTools(gdpData, year)
			visualAnalysisTools.saveGraphs()
		print 'The plots have been saved. Please check your current directory for the files.'
		
	except KeyboardInterrupt:
		print 'Good bye.'

main()
