#!/usr/bin/python3

from tkinter import *
from control import Control
from navigation import Navigation
from makestuff import MakeFrame
from view import View
from functools import partial

# mess.py
# JS OT Bristol 2018


class Application():
    def __init__(self):

        # layout window
        self.setgeometry()
        # create background frames
        self.buildframes()

        # Make view object...
        self.view = View(self.viewframe.frame)
        self.view.make_label("Hello",0)
        self.view.make_text_entry("Other label",partial(print,1))
        self.view.set_output("This is the output",2)
        self.view.set_output("This more output",3)
        
        # make control object
        self.control = Control(self.controlframe.frame)

        # exit buttons
        self.navigation = Navigation(self.root, self.exitframe.frame,self.docframe.frame, self.control)

        # Run it all!
        self.root.mainloop()

    def setgeometry(self):
        # make window called self.root
        self.root = Tk()
        # dimensions of window
        self.winwidth = 640
        self.winheight = 480
        self.root.minsize(920, 480)
        # geometry
        self.root.resizable(width=True, height=True)
        self.root.geometry('{}x{}'.format(self.winwidth, self.winheight))
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

        # get that professional font
        font = ('Comic Sans MS', 12)
        self.root.option_add("*Font", font)

    def buildframes(self):
        # make frames for backgrounds and splitting the widgits
        self.docframe = MakeFrame(self.root, 'lime', 100, 100, 0, 0, 'nesw')
        self.viewframe = MakeFrame(self.root, 'yellow', 100, 100, 1, 0, 'nsew')
        self.controlframe = MakeFrame(self.root, 'white', 100, 100, 2, 0,'nsew')
        self.exitframe = MakeFrame(self.root, 'cyan', 100, 100, 3, 0, 'nsew')



        
APP = Application()
