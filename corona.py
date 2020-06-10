#!/usr/bin/python3
'''
Eric Sullivan
05/30/2020
Rewritting my Covid-19 plot script in python 3
the old script is pretty scuff, so I would like
to try and improve it with this one.

This uses the John-Hopkins Git repository for Corona
statisctics.
'''
import sys
import csv
import re
import numpy as np
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as md
from pandas.plotting import register_matplotlib_converters

class CovidData:

    def __init__(self, url):
        self.data = self.downloadData(url)
        self.dates = self.convertDates(self.formatData())
        # Needed for conversions
        register_matplotlib_converters()

    def downloadData(self, url):
        '''
        Downloads data from John Hopkins Covid Github, and
        stores it into a pandas data frame
        '''
        try:
            df = pd.read_csv(url)
            df = df.fillna('0')
            return df
        except:
            print("Error! Url not valid or unable to access repository!")
            return None
    
    def formatData(self):
        '''
        Formats data frame so it only has the date columns - This is for graphing
        the accumulative total of cases/deaths.
        '''
        # Gets a hard copy of the current data frame
        df = self.data.copy()
        if df.empty:
            print("Error! No data to format")
            return None
        for i in df.columns:
            dateFound = re.search(r'([0-9]?[0-9])/([0-9]?[0-9])/([0-9][0-9])', i)
            if dateFound is not None:
                break
            else:
                df= df.drop([i], axis = 1)
                
        if dateFound is None:
            print("Error! No dates found in the data")
            return None
        else:
            return df

    def convertDates(self, df):
        '''
        Converts dates from graphs into datetime objects
        for the graphs
        '''
        dates = []
        if df.empty:
            print("Error! No data present")
            return None
        try:
            for i in df.columns:
                dates.append(datetime.datetime.strptime(i, "%m/%d/%y"))
            
            return dates

        except:
            print("Error! Probelm with getting dates!")
            return None

    def plotData(self, label, linetype, rate = False):
        df = self.formatData()
        dates = md.date2num(self.dates)
        dataPoints = df.to_numpy()

        sumPoints = []
        for i in range(dataPoints.shape[1]):
            sumPoints.append(np.sum(dataPoints[:, i]))

        # This is if you want to see the cases/deaths per day
        if rate is True:
            rate = []
            rate.append(sumPoints[0])
            for i in range(1, len(sumPoints)):
                rate.append(sumPoints[i] - sumPoints[i-1])
            
            plt.plot_date(dates, rate, linetype, label = label)
        else:
            plt.plot_date(dates, sumPoints, linetype, label = label)

    def showPlot(self):
        plt.grid(linestyle='-', linewidth = 2)
        plt.xlabel("Date")
        plt.ylabel("Number of People")
        plt.legend()
        plt.show()



if __name__ == '__main__':
    deathsUSurl = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv'
    confirmedUSurl = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv'
    
    death = CovidData(deathsUSurl)
    #print(death.data)
    #print(death.data.iloc[:,2])
    #print(death.data.columns[1])
    death.plotData("Deaths: US", 'r-', True)
    death.showPlot()
    confirmed = CovidData(confirmedUSurl)
    confirmed.plotData("Confirmed: US", 'b-', True)
    confirmed.showPlot()