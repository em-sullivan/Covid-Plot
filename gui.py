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
        self.usCases["command"] = self.plotAllConfrimedUS
        self.usCases.pack(side = "top")

        self.quit = tk.Button(self, text = "Quit", fg = "red", command = self.master.destroy)
        self.quit.pack(side = "bottom")

    def plotAllDeathsUS(self):
        deaths = CovidData('https://tinyurl.com/vxbdvgo')
        deaths.plotData("Total Deaths in the US", 'r-')

    def plotAllConfrimedUS(self):
        confirmed = CovidData('https://tinyurl.com/uynhaxd')
        confirmed.plotData("Total Confrimed Covid Cases in the US", 'b-')


root = tk.Tk()
app = App(master = root)
app.mainloop()