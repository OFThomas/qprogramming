# control.py
# JS OT Bristol 2018

from functools import partial

from makestuff import *
from quantumprograms import *


class Control():
    def __init__(self, frame):
        self.frame = frame
        self.labels = []
        self.buttons = {}
        self.row, self.column = 0, 0

    # Return values:
    #   0 = success
    #   1 = not enough space for button
    #   2 = duplicate key
    #
    def AddButton(self, label, cmd, key=0):
        if key in self.buttons:
            return 2
        if self.row == 3 and self.column == 0:
            return 1

        print('cmd', cmd)
        self.buttons[key] = MakeButton(self.frame, 2, 0, label, cmd)
        self.buttons[key].button.grid(row=self.row, column=self.column)
        self.column = self.column + 1
        if self.column == 2:
            self.column = 0
            self.row = self.row + 1
        return 0

    def clear_all(self):
        for key in self.buttons:
            self.buttons[key].destroy()
        self.row = 0
