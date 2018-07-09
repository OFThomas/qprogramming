# control.py
# JS OT Bristol 2018

from functools import partial

from makestuff import MakeButton

class Control():
    def __init__(self, frame):
        self.frame = frame
        self.labels = []
        self.buttons = {}
        self.row, self.column = 0, 0
        self.state = 0
    # Return values:
    #   0 = success
    #   1 = not enough space for button
    #   2 = duplicate key
    #
    def __addbutton(self, label, cmd, key=0):
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

    # Takes a list of button labels and functions
    # that the button should execute. The format of
    # the list is
    #
    # list = [ [label1, function1],
    #          [label2, function2],
    #             .          .
    #             .          .
    #             .          .
    #          [labelN, functionN] ]
    #
    # The function is in the form partial(fun,args)
    #
    def make_screen(self,lst):
        # Get the number of buttons
        N = len(lst)
        for key in range(N):
            self.__addbutton(lst[key][0],lst[key][1],key)
    
    def go_back(self):
        print("back")

    def go_home(self):
        print("home")    
    
    def clear_all(self):
        for key in self.buttons:
            self.buttons[key].destroy()
        self.row = 0
