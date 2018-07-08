from functools import partial
from tkinter import *

from makestuff import MakeButton

# exits.py
# JS OT Bristol 2018


class Exits():
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame
        # exit buttons
        self.makeexit()
    
    def makeexit(self):
        self.exitlabels = [['Back', partial(print, 'back')],
                           ['Home', partial(print, 'Home')],
                           ['Exit', partial(self.root.destroy)]]
        exitbutton = [None] * len(self.exitlabels)

        for i in range(0, len(self.exitlabels)):
            exitbutton[i] = MakeButton(self.frame, 0, i,
                                       self.exitlabels[i][0],
                                       self.exitlabels[i][1])

