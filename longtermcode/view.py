from tkinter import *

from makestuff import *


# Class for handling user interactions in the input output area
# Takes two MakeFrame objects as arguments in the constructor.
#
class View():

    # Constructor
    # Create empty dictionaries for storing textboxes, buttons,
    # labels etc.
    def __init__(self, masterframe):
        self.root = masterframe
        self.iframe = MakeFrame(self.root, 'red', 100, 100, 0, 0, 'nsew').frame
        self.oframe = MakeFrame(self.root, 'orange', 100, 100, 0, 1,
                                'nsew').frame
        self.input = {}
        self.output = {}
        self.irow, self.orow = 0, 0

    def make_label(self, text, label):
        self.input[label] = Label(self.iframe, text=text)
        self.input[label].grid(row=self.irow, column=0)
        self.irow = self.irow + 1

    def make_text_entry(self, label, cmd):
        self.input[label] = Entry(self.iframe, bd=0)
        self.input[label].grid(row=self.irow, column=0)
        self.input[label].bind("<Return>", cmd)
        self.irow = self.irow + 1

    def make_button(self, label, cmd):
        self.input[label] = MakeButton(self.iframe, 2, 0, "Submit", cmd)
        self.input[label].button.grid(row=self.irow, column=0)
        self.irow = self.irow + 1

    def make_input_box(self, text, cmd):
        self.make_label(text, "input_label")
        ## need to do lambda event: ... for binds
        self.make_text_entry("insert_box",
                             lambda event: cmd(self.input["insert_box"].get()))
        self.make_button("insert_button",
                         lambda: cmd(self.input["insert_box"].get()))

    def get_answer(self):
        return self.input["insert_box"].get()

    def set_output(self, text, label):
        for key in self.output:
            self.output[key].destroy()

        self.output[label] = Message(self.oframe, text=text)
        self.output[label].grid(row=self.orow, column=0)
        self.orow = self.orow + 1

    def clear_all(self):
        for key in self.input:
            self.input[key].destroy()

        for key in self.output:
            self.output[key].destroy()

        self.irow, self.orow = 0, 0

    def run_function(self, fun):
        self.clear_all()
        print("What I'm about to run IN FUN:", fun)
        # fun()
