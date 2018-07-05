#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showinfo
import webbrowser
from makestuff import *
from control import *

class Background(Frame):
    #open different windows
    
    def __init__(self,location):
        self.buildframe(location) 
        # documentation
        self.control=Control(self.controlframe.frame)
        #self.root.mainloop()        

    def buildframe(self, location):
        #make frames for backgrounds and splitting the widgits
        self.docframe=MakeFrame(location, 'lime', 100,100,0,0,'nesw')
        self.viewframe = MakeFrame(location,'black',100,100,1,0,'nsew')
        self.controlframe = MakeFrame(location, 'white',200, 100,2,0,'nsew')  
        self.exitfram=MakeFrame(location, 'cyan', 100,100,3,0,'nsew')
        return 

    def makedocs(self):
         self.doclabels=[['Quantum programming guide',partial(print, 'q prog')], 
                ['Riggeti docs',partial(print,'rigetti docs'],
                ['Qiskit docs',partial(print, 'qiskit docs'],
                ['Project Q docs',partial(print, 'projectq']]



