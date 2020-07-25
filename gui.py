#!/usr/bin/python3

import tkinter as tk
import matplotlib.pyplot as plt
from corona import CovidData

class App(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.master.title('Covid-19 Tracker')
        self.pack()
        
        # Bools for graphing rate or if a figure exsits
        self.rateVar = tk.IntVar()
        self.figExsists = tk.IntVar()

        # Vars to determine what needs to be graphed
        self.subjs = []
        for i in range(5):
            self.subjs.append(tk.IntVar())
        
        self.create_widgets()

    def create_widgets(self):
        
        self.deathUS = tk.Checkbutton(self, text = 'Deaths US', variable = self.subjs[0])
        self.deathUS.pack(side = "top")

        self.rates = tk.Checkbutton(self, text = 'Daily Rate', variable = self.rateVar)
        self.rates.pack(side = "right")
        
        self.confirmedUS = tk.Checkbutton(self, text = 'Confirmed US', variable = self.subjs[1])
        self.confirmedUS.pack(side = "top")

        self.deathWorld = tk.Checkbutton(self, text = 'Deaths World', variable = self.subjs[2])
        self.deathWorld.pack(side = "top")

        self.confirmedUS = tk.Checkbutton(self, text = 'Confirmed World', variable = self.subjs[3])
        self.confirmedUS.pack(side = "top")

        self.recoveredWorld = tk.Checkbutton(self, text = 'Recovered World', variable = self.subjs[4])
        self.recoveredWorld.pack(side = "top") 

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
    
    def plotAll(self):

        atLeastOne = False

        dataUrls = ['https://tinyurl.com/vxbdvgo',
            'https://tinyurl.com/uynhaxd',
            'https://tinyurl.com/rlssflz',
            'https://tinyurl.com/tsqkf7y',
            'https://tinyurl.com/vtcebxt']

        colors = ['#ff4500', 'c-', 'r-', 'b-', 'g-']

        labels = ["Deaths: US",
            "Confirmed Cases: US",
            "Deaths: World",
            "Confirmed: World",
            "Recovered: World"]

        if plt.get_fignums():
            print("Figure already exsits!")
            return

        rate = self.checkBool(self.rateVar)
        
        for i in range(5):
            if self.checkBool(self.subjs[i]):
                data = CovidData(dataUrls[i])
                data.plotData(labels[i], colors[i], rate)
                atLeastOne = True

        if atLeastOne is True:
            if rate is True:
                data.showPlot("Cases by Day")
            else:
                data.showPlot("Accumulative Cases")
        else:
            print("There is nothing to graph!")


root = tk.Tk()
app = App(master = root)
app.mainloop()