#!/usr/bin/python3
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
        #make background frames on self.root
        Background(self.root)     
        #end 
        self.root.mainloop()    
  
    def setgeometry(self):
        # make window called self.root
        self.root = Tk()
        #dimensions of window 
        self.winwidth=640
        self.winheight=480
        #geometry 
        self.root.resizable(width=TRUE,height=TRUE)
        self.root.geometry('{}x{}'.format(self.winwidth,self.winheight))
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        
        #get that professional font
        font=('Comic Sans MS', 15)
        self.root.option_add("*Font", font)
        
app=Application()
