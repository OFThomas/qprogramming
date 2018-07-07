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
from control import *
from view import *
from quantumprograms import *
from functools import partial 

class Application(Frame):

    def __init__ (self):

        #layout window
        self.setgeometry()
        # create background frames
        self.buildframe() 
        # documentation
        self.makedocs()
        # Make view object...
        self.view = View(self.viewframe.frame)
        # make control object
        self.control=Control(self.controlframe.frame)
        # exit buttons
        self.makeexit()
        # Run it all!
        self.root.mainloop()    
  
    def setgeometry(self):
        # make window called self.root
        self.root = Tk()
        #dimensions of window 
        self.winwidth=920
        self.winheight=480
        self.root.minsize(920,480)
        #geometry 
        self.root.resizable(width=TRUE,height=TRUE)
        self.root.geometry('{}x{}'.format(self.winwidth,self.winheight))
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        
        #get that professional font
        font=('Comic Sans MS', 12)
        self.root.option_add("*Font", font)

    def buildframe(self):
        #make frames for backgrounds and splitting the widgits
        self.docframe=MakeFrame(self.root, 'lime', 100,100,0,0,'nesw')
        self.viewframe = MakeFrame(self.root,'yellow',100,100,1,0,'nsew')
        self.controlframe = MakeFrame(self.root, 'white',100,100,2,0,'nsew')
        self.exitframe=MakeFrame(self.root, 'cyan', 100,100,3,0,'nsew')
        return 

    def makedocs(self):
         self.doclabels=[['Quantum programming guide',partial(print, 'q prog')], 
                ['Riggeti docs',partial(print,'rigetti docs')],
                ['Qiskit docs',partial(print, 'qiskit docs')],
                ['Project Q docs',partial(print,'project Q')]]
         
         docbutton=[None]*len(self.doclabels)
         for j in range(0,1):
             for i in range(0,int(len(self.doclabels))):
                 count=i+2*j
                 docbutton[count]=MakeButton(self.docframe.frame,
                         j,i,self.doclabels[count][0],
                         self.doclabels[count][1])
        
    def makeexit(self):
        self.exitlabels=[['Back',partial(print, 'back')],['Home', partial(print, 'Home')],['Exit', partial(self.root.destroy)]]
        exitbutton=[None]*len(self.exitlabels)
        for i in range(0,len(self.exitlabels)):
            exitbutton[i]=MakeButton(self.exitframe.frame, 0,i,
                                     self.exitlabels[i][0],
                                     self.exitlabels[i][1])


        
app=Application()
