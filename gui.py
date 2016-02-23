#!/usr/bin/python2.7

from Tkinter import *
import tkMessageBox
import math

velocity=0.0
mass=10
windvel=0
power=0
time=0.0
g=9.8
pointx=0
pointy=0
time=0
angle=0
player=TRUE  #true if player 1's turn false if player 2's turn

def firecallback(f,s) :
	velocity=f/10
	power=f
	angle=s*math.pi/180
	tkMessageBox.showinfo("Values","power : %s angle: %s  " % (velocity,power))
	if player==TRUE :
		while player==TRUE:
			timefunc_player1()
	else :
		while player==FALSE:
			timefunc_player2()


def timefunc_player1():
	pointx=((velocity)*math.cos(angle)+windvel)*time
	pointy=velocity*math.sin(angle)-0.5*g*time*time

def timefunc_player2():
	pointx=((velocity)*math.cos(angle)+windvel)*time
	pointy=velocity*math.sin(angle)-0.5*g*time*time

root = Tk()
root.geometry('640x480')
C = Canvas(root, bg = "black", height = 360, width = 640)
controls = Frame(root, height = 120, width = 640)
var = 0
scale = Scale(controls, variable = var, bg = "LIGHTYELLOW", orient = HORIZONTAL, width = 20, label = "POWER", troughcolor = "RED" ).grid(row = 1, column = 1, rowspan = 1, columnspan = 2)
var2 = 0
scale2 = Scale(controls, variable = var2, bg = "LIGHTGREEN", orient = HORIZONTAL, width = 20, label = "Angle", troughcolor = "LIGHTBLUE", length = 100, from_ = 0, to = 360).grid(row = 2, column = 1, rowspan = 1, columnspan = 2)
fire = Button(controls,command=lambda x=var, y=var2: firecallback(x,y), text = "FIRE", height  = 5, width = 48, justify = CENTER, activeforeground = "WHITE", activebackground = "RED").grid(row = 1, column = 3, rowspan = 2, columnspan = 2)
wind = Canvas (controls, bg = "CYAN", height = 120, width = 120).grid(row = 1, column = 5, rowspan = 2, columnspan = 2)
controls.pack(side = BOTTOM)
C.pack()

mainloop()