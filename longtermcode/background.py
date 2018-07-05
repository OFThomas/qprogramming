#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showinfo
import webbrowser
from makestuff import *

class Background(Frame):
    #open different windows
    
    def __init__(self):
        self.setgeometry() 
        #make frames for backgrounds and splitting the widgits
        self.view = MakeFrame(self.root,'black',100,100,0,0,'nsew')
        self.input = MakeFrame(self.view.frame,'green',100,100,0,0,'nsew')
        self.output = MakeFrame(self.view.frame,'pink',100,100,0,1,'nswe')
        #here be buttons 
        self.control = MakeFrame(self.root, 'white',200, 40,1,0,'nsew')  
        self.interact = MakeIO(self.input,self.output)
        # documentation
        self.docframe=MakeFrame(self.root, 'lime', 100,100,20,0,'nesw')
       
        doclabels=[['Quantum programming guide',lambda:None], 
                ['Riggeti docs',lambda:None],
                ['Qiskit docs',lambda:None],
                ['Project Q docs',lambda:None]]

        #for i in range(0,len(doclabels)):
        #    self.Bdocs[i]=MakeButton(self.docframe.frame, i,0,)

        self.colors=['blue', 'yellow', 'green', 'orange', 'cyan', 'purple']
        

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
        return 

backgroundframe=Background()
