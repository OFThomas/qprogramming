from functools import partial
from tkinter import *
from makestuff import MakeButton
import webbrowser

# exits.py
# JS OT Bristol 2018


class Navigation():
    def __init__(self, root, frame, docs, control):
        self.docs = docs
        self.control = control
        self.root = root
        self.frame = frame
        # All buttons!
        self.doclabel = 'Q programming guide'
        self.url = 'https://www.google.com/'
        self.top()
        self.bottom()

    def top(self):
        guide_doc = MakeButton(self.docs, 0, 0, self.doclabel,
                               partial(webbrowser.open, self.url))
        
    def bottom(self):
        self.exitlabels = [['Back', partial(self.control.go_back)],
                           ['Home', partial(self.control.go_home)],
                           ['Exit', partial(self.root.destroy)]]
        exitbutton = [None] * len(self.exitlabels)

        for i in range(0, len(self.exitlabels)):
            exitbutton[i] = MakeButton(self.frame, 0, i,
                                       self.exitlabels[i][0],
                                       self.exitlabels[i][1])
