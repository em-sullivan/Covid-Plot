#!/usr/bin/python3

import tkinter as tk
from corona import CovidData

class App(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.pack()
        
        # Bools for graphing rate or if a figure exsits
        self.rateVar = tk.IntVar()
        self.figExsists = tk.IntVar()

        self.subjs = []
        for i in range(5):
            self.subjs.append(tk.IntVar())

        self.create_widgets()

    def create_widgets(self):
        self.usDeaths = tk.Button(self)
        self.usDeaths["text"] = "US Covid Deaths"
        self.usDeaths["command"] = self.plotAllDeathsUS
        self.usDeaths.pack(side = "top")

        self.rates = tk.Checkbutton(self, text = 'Daily Rate', variable = self.rateVar)
        self.rates.pack(side = "right")

        self.usCases = tk.Button(self, text = "US Confirmed Covid Cases")
        self.usCases["command"] = self.plotAllConfirmedUS
        self.usCases.pack(side = "top")

        self.worldDeaths = tk.Button(self, text = "World Covid Deaths")
        self.worldDeaths["command"] = self.plotAllDeathsWD
        self.worldDeaths.pack(side = "top")

        self.worldConfirmed = tk.Button(self, text = "World Confirmed Covid Cases")
        self.worldConfirmed["command"] = self.plotAllConfirmedWD
        self.worldConfirmed.pack(side = "top")

        self.worldRecoverd = tk.Button(self, text = "World Recovered Covid Cases")
        self.worldRecoverd["command"] = self.plotAllRecoveredWD
        self.worldRecoverd.pack(side = "top") 

        self.deathus = tk.Checkbutton(self, text = 'Deaths US', variable = self.subjs[0])
        self.deathus.pack(side = "right")

        self.plotButton = tk.Button(self, text = "Plot")
        self.plotButton["command"] = self.plotAll
        self.plotButton.pack(side = "top")

        self.quit = tk.Button(self, text = "Quit", fg = "red", command = self.master.destroy)
        self.quit.pack(side = "bottom")
    
    def checkBool(self, val):
        if val.get() == 1:
            return True
        else:
            return False

    def plotAllDeathsUS(self):
        
        rate = self.checkBool(self.rateVar)
        deaths = CovidData('https://tinyurl.com/vxbdvgo')
        deaths.plotData("Total Deaths in the US", '#ff4500', rate)
        del(deaths)

    def plotAllConfirmedUS(self):
        rate = self.checkBool(self.rateVar)
        confirmed = CovidData('https://tinyurl.com/uynhaxd')
        confirmed.plotData("Total Confrimed Covid Cases in the US", 'c-', rate)
        del(confirmed)
    
    def plotAllDeathsWD(self):
        rate = self.checkBool(self.rateVar)
        deaths = CovidData('https://tinyurl.com/rlssflz')
        deaths.plotData("Total Deaths Globally", 'r-', rate)
        del(deaths)

    def plotAllConfirmedWD(self):
        rate = self.checkBool(self.rateVar)
        confirmed = CovidData('https://tinyurl.com/tsqkf7y')
        confirmed.plotData("Total Confirmed Covid Cases WorldWide", 'b-', rate)
        del(confirmed)

    def plotAllRecoveredWD(self):
        rate = self.checkBool(self.rateVar)
        recovered = CovidData('https://tinyurl.com/vtcebxt')
        recovered.plotData("Total Recovered Cases WorldWide", 'g-', rate)
        del(recovered)
    
    def plotAll(self):
        rate = self.checkBool(self.rateVar)
        if self.checkBool(self.subjs[0]):
            deaths = CovidData('https://tinyurl.com/vxbdvgo')
            deaths.plotData("Total Deaths in the US", '#ff4500', rate)
            (deaths)


root = tk.Tk()
app = App(master = root)
app.mainloop()