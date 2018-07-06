from makestuff import *
from functools import partial 
from quantumprograms import *
class Control():

    def __init__(self,frame):
        self.frame = frame
        self.buttons = {}
        self.row, self.column = 0,0
        
    def make_button(self,label,cmd):
        print('cmd', cmd)
        self.buttons[label] = MakeButton(self.frame,2,0,"Submit",cmd)
        self.buttons[label].button.grid(row=self.row,column=self.column)
        self.column = self.column + 1 
        if self.column == 2:
            self.column = 0
            self.row = self.row + 1
            if self.row == 3: exit(1)

    def clear_all(self):
        for key in self.input:
            self.buttons[key].destroy()
        self.row = 0

