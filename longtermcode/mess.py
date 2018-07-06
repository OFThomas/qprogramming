#!/usr/bin/python3

# mess.py
# JS OT Bristol 2018

from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showinfo
import webbrowser
#what the buttons actually do...
from quantumprograms import *
#constructors
from makestuff import *
from background import *
from control import *
from quantumprograms import *

class Application(Frame):

    def __init__ (self):
        #layout window
        self.setgeometry()

        # make bg frames
        self.background=Background(self.root)
        
        # make control buttons
        self.control=Control(self.background.controlframe.frame)
        
        result=self.control.AddButton('txt', partial(print, 'tst'))

        #end 
        self.root.mainloop()    
  
    def setgeometry(self):
        # make window called self.root
        self.root = Tk()
        #dimensions of window 
        self.winwidth=1280
        self.winheight=720
        #geometry 
        self.root.resizable(width=TRUE,height=TRUE)
        self.root.geometry('{}x{}'.format(self.winwidth,self.winheight))
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        
        #get that professional font
        font=('Comic Sans MS', 12)
        self.root.option_add("*Font", font)

app=Application()
