#!/usr/bin/python3

import tkinter as tk
from corona import CovidData

class App(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.usDeaths = tk.Button(self)
        self.usDeaths["text"] = "US Covid Deaths"
        self.usDeaths["command"] = self.plotAllDeathsUS
        self.usDeaths.pack(side = "top")

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

        self.quit = tk.Button(self, text = "Quit", fg = "red", command = self.master.destroy)
        self.quit.pack(side = "bottom")

    def plotAllDeathsUS(self):
        deaths = CovidData('https://tinyurl.com/vxbdvgo')
        deaths.plotData("Total Deaths in the US", '#ff4500')
        del(deaths)

    def plotAllConfirmedUS(self):
        confirmed = CovidData('https://tinyurl.com/uynhaxd')
        confirmed.plotData("Total Confrimed Covid Cases in the US", 'c-')
        del(confirmed)
    
    def plotAllDeathsWD(self):
        deaths = CovidData('https://tinyurl.com/rlssflz')
        deaths.plotData("Total Deaths Globally", 'r-')
        del(deaths)

    def plotAllConfirmedWD(self):
        confirmed = CovidData('https://tinyurl.com/tsqkf7y')
        confirmed.plotData("Total Confirmed Covid Cases WorldWide", 'b-')
        del(confirmed)

    def plotAllRecoveredWD(self):
        recovered = CovidData('https://tinyurl.com/vtcebxt')
        recovered.plotData("Total Recovered Cases WorldWide", 'g-')
        del(recovered)

root = tk.Tk()
app = App(master = root)
app.mainloop()