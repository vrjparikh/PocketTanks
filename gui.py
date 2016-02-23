#!/usr/bin/python2.7

from Tkinter import *

root = Tk()
root.geometry('640x480')
C = Canvas(root, bg = "black", height = 360, width = 640)
controls = Frame(root, height = 120, width = 640)
var = DoubleVar()
scale = Scale(controls, variable = var, bg = "LIGHTYELLOW", orient = HORIZONTAL, width = 20, label = "POWER", troughcolor = "RED" ).grid(row = 1, column = 1, rowspan = 1, columnspan = 2)
var2 = DoubleVar()
scale2 = Scale(controls, variable = var2, bg = "LIGHTGREEN", orient = HORIZONTAL, width = 20, label = "Angle", troughcolor = "LIGHTBLUE", length = 100, from_ = 0, to = 360).grid(row = 2, column = 1, rowspan = 1, columnspan = 2)
fire = Button(controls, text = "FIRE", height  = 5, width = 48, justify = CENTER, activeforeground = "WHITE", activebackground = "RED").grid(row = 1, column = 3, rowspan = 2, columnspan = 2)
wind = Canvas (controls, bg = "CYAN", height = 120, width = 120).grid(row = 1, column = 5, rowspan = 2, columnspan = 2)
controls.pack(side = BOTTOM)
C.pack()
mainloop()