#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import tkinter as tk
from math import sqrt

import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class QuadraticFunction:
	def __init__(self, a, b, c):
		try:
			self.roots = [None, None]
			self.a = float(a)
			self.b = float(b)
			self.c = float(c)
		except ValueError:
			self.roots[0] = "Given data is not a number"
		else:
			self.calculateRoots()
	
	def calculateRoots(self):
		if self.roots[0] is None:
			if self.a == 0:
				self.roots[0] = "Given function is not quadratic"
			else:
				delta = self.b ** 2 - 4 * self.a * self.c
				if delta < 0:
					self.roots[0] = "Given function has no roots"
				elif delta == 0:
					self.roots[0] = (-self.b) / (2 * self.a) + 0
				else:
					self.roots[0] = (-self.b - sqrt(delta)) / (2 * self.a) + 0
					self.roots[1] = (-self.b + sqrt(delta)) / (2 * self.a) + 0


def getRange():
    return range(-10, 11) 

window = tk.Tk()
window.title("Parables")
window.geometry("500x800")
labels = []
entries = []

for i in range(0, 3):
    l = tk.Label(window)
    if i == 0:
        l["text"] ="a: "
    elif i == 1:
        l["text"] ="b: "
    elif i == 2:
        l["text"] ="c: "
    l.grid(row=i, column=1)
    labels.append(l)
    e = tk.Entry(window, font=("Arial", 14))
    e.grid(row=i, column=2)
    entries.append(e)
label = tk.Label(window)
label.grid(row=4, column=1, rowspan=2, columnspan=3)
def onclick():
    a = entries[0].get()
    b = entries[1].get()
    c = entries[2].get()

    if a == '' or b == '' or c == '':
        l["text"] = "Specify a, b and c!"
    else:
        qF = QuadraticFunction(a, b, c)
        if isinstance(qF.roots[0], str):
        	label["text"] = qF.roots[0]
        elif qF.roots[1] is None:
        	label["text"] = "Given function has 1 root\n in " + f"{qF.roots[0]:g}"
        else:
        	label["text"] = "Given fucntion has 2 roots\n in " + f"{qF.roots[0]:g}" + " and " + f"{qF.roots[1]:g}"

        a = float(a)
        b = float(b)
        c = float(c)

        x = getRange()
        y = [a * (x**2) + b * x + c for x in getRange()]
        
        fig = Figure(figsize=(5, 5), dpi=100)
        plot = fig.add_subplot()
        plot.grid()
        plot.plot(x, y)

        graphPage = tk.Frame(window)
        graphPage.grid(row=6, column=1, columnspan=3)

        mplCanvas = FigureCanvasTkAgg(fig, master=graphPage)
        mplCanvas.draw()
        mplCanvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)


b = tk.Button(window, command=onclick, text="Click to calc roots and draw graph")
b.grid(row=3, column=1, columnspan=3)

window.mainloop()