# Developer: Byung Woong Ko
# Start Date: 15JAN2023
# Project: Operation Valentine

# Description: This Project will have executable which sends out a prank "hacked" message 
# followed by a "will you be my valentine" message. If yes it will play a prerecorded video.
# If not it will say please for 5 iterations which it will then display obseneties.

import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
import os
from os import startfile

count = 0
mb.showinfo('Hacked', 'Your computer has been hacked. LOL')
mb.showinfo('Hacked', 'But I have one question for you...')
res= mb.askyesno('Hacked', 'Will you be my Valentine?')
while (res == False and count < 5):
    count=count+1
    res= mb.askyesno('Hacked', 'Please?')
if (res == False and count==5):
    mb.showinfo("Hacked", 'Fuck you')
else:
    mb.showinfo("Hacked", 'Love you bby^^')
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    f =os.path.join(location, 'Valentine.MOV')
    startfile(f)