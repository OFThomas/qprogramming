#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showinfo
import webbrowser
from makestuff import *
from control import *

class Background(Frame):
    #open different windows
    
    def __init__(self):
        self.setgeometry() 
        self.buildframe() 
        #here be buttons 
        # documentation
        self.control=Control(self.controlframe.frame)
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
        
    def buildframe(self):
        #make frames for backgrounds and splitting the widgits
        self.docframe=MakeFrame(self.root, 'lime', 100,100,0,0,'nesw')
        self.viewframe = MakeFrame(self.root,'black',100,100,1,0,'nsew')
        self.controlframe = MakeFrame(self.root, 'white',200, 100,2,0,'nsew')  
        self.exitfram=MakeFrame(self.root, 'cyan', 100,100,3,0,'nsew')
        return 

    def makedocs(self):
         doclabels=[['Quantum programming guide',lambda:None], 
                ['Riggeti docs',lambda:None],
                ['Qiskit docs',lambda:None],
                ['Project Q docs',lambda:None]]
        #self.b0=MakeButton()


backgroundframe=Background()
