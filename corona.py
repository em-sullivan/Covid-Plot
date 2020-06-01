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

class CovidData:

    def __init__(self, url, label):
        self.label = label
        self.data = self.downloadData(url)
        self.dates = []

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
        Formats Data
        '''
        if self.data.empty:
            print("Error! No data to format")
            return
        for i in self.data.columns:
            dateFound = re.search(r'([0-9]?[0-9])/([0-9]?[0-9])/([0-9][0-9])', i)
            if dateFound is not None:
                break
            else:
                self.data = self.data.drop([i], axis = 1)
                
        #if dateFound is None:
        #    return
        #self.npdata = self.data.to_numpy()
        #print(dateFound.group(0))
        #print(self.data)
        #print(self.npdata)

    def convertDates(self):
        if self.data.empty:
            print("Error! No data present")
            return
       
        for i in self.data.columns:
            self.dates.append(datetime.datetime.strptime(i, "%m/%d/%y"))
        print(self.dates)

    def plotData(self):
        self.formatData()
        self.convertDates()
        self.dates = md.date2num(self.dates)
        dataPoints = self.data.to_numpy()

        sumPoints = []
        for i in range(dataPoints.shape[1]):
            sumPoints.append(np.sum(dataPoints[:, i]))
        
        plt.plot_date(self.dates, sumPoints, 'r-')
        plt.title(self.label)
        plt.grid(linestyle='-', linewidth = 2)
        plt.xlabel("Date")
        plt.ylabel("Number of People")
        plt.show()



if __name__ == '__main__':
    deathsUSurl = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv'
    
    death = CovidData(deathsUSurl, "usdeaths")
    print(death.data)
    print(death.data.iloc[:,2])
    print(death.data.columns[1])
    #death.formatData()
    #death.convertDates()
    death.plotData()