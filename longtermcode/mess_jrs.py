from tkinter import *
from tkinter import messagebox
from functools import partial
from shor import shor

class OpenToplevels(Frame):
    #open different windows
    def __init__(self):
        self.root = Tk()
        self.button_ctr=0
        
        menubut=Button(self.root, text='Work pls', command=self.menus)
        menubut.grid(row=0, column=0)
                
        Button(self.root, text="Exit Tkinter", bg="red",
                  command=self.root.quit).grid(row=1, column=0, sticky="we")
        self.root.mainloop()
    
    def menus(self):
        self.button_ctr += 1
        id = Toplevel(self.root)
        id.title("Toplevel #%d" % (self.button_ctr))
        Button(id, text="Close Toplevel #%d" % (self.button_ctr),
                  command=partial(self.close_it, id),
                  bg="orange", width=20).grid(row=100, column=0)
        
        hi_there = Button(id, fg="white", bg="blue")
        hi_there["text"] = "Hello World\n Do you want to do some quantum programming? \n(click me)"
        # do stuff
        hi_there["command"] = self.begin()
        #put at the top of the screen
        hi_there.grid(row=0, column=0)

    def begin(self):
        print("hi there, everyone!")

    def close_it(self, id):
        id.destroy()

ot=OpenToplevels()
