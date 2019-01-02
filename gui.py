# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 14:29:40 2018

@author: arcse
"""
from interface import *
import tkinter as tk
 
from playsound import playsound
import sys
 

top=tk.Tk() 
top.geometry("1600x1200")
top.configure(background='#87CEFA')
top.title("Interface")

W_l=tk.Label(top,text="Say 1 for live object detection") 
W_l.config(font=("Courier", 20))
W_l.pack()

W_i=tk.Label(top,text="Say 2 for image's text to speech conversion") 
W_i.config(font=("Courier", 20))
W_i.pack()

W_e=tk.Label(top,text="Say 0 for exit from system") 
W_e.config(font=("Courier", 20))
W_e.pack()

start_button=tk.Button(top,text="Click anywhere to start the program",bg='#FAEBD7',fg='green',height='100',font=("Courier", 25),width='280',command= choices)
start_button.pack()
playsound("st6.mp3")

top.mainloop()

