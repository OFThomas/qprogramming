from tkinter import *
from tkinter import messagebox
from functools import partial
from shor_alg import shor
import webbrowser

class OpenToplevels(Frame):
    #open different windows
    def __init__(self):
        #self.shor = shor
        self.root = Tk()
        self.button_ctr=0

        hi_there = Button(self.root, fg="white", bg="blue")
        hi_there["text"] = "Hello World\n Do you want to do some quantum programming? \n(click me)"
        # do stuff
        hi_there["command"] = self.begin()
        #put at the top of the screen
        hi_there.grid(row=0, column=0)
        projectq=Button(self.root, text="Project Q this way!", command=run_projectq).grid(row=1,column=0)
        pyquil=Button(self.root, text="Pyquil", command=run_pyquil).grid(row=1,column=1)
        qiskit=Button(self.root, text="qiskit", command=run_qiskit).grid(row=2,column=0)
        qsharp=Button(self.root, text="qsharp", command=run_qsharp).grid(row=2,column=1)
        test=Button(self.root, text="shor", command=lambda:shor(15)).grid(row=3,column=0)
        
        Button(self.root, text="Exit Tkinter", bg="red",
                  command=self.root.quit).grid(row=100, column=0, sticky="we")
        self.root.mainloop()
    
    def menus(self):
        self.button_ctr += 1
        '''
        id = Toplevel(self.root)

        id.title("Toplevel #%d" % (self.button_ctr))


        Button(id, text="Close Toplevel #%d" % (self.button_ctr),
                  command=partial(self.close_it, id),
                  bg="orange", width=20).grid(row=100, column=0)
        '''
        
    def begin(self):
        print("hi there, everyone!")
        webbrowser.open("https://github.com/ot561/qprogramming/report/main.pdf")

    def close_it(self, id):
        id.destroy()

def run_shor():
    shor(n)
        
def run_projectq():
    print('Pq')

def run_qsharp():
    print('NO Q# for you')

def run_qiskit():
    print('qiskit')

def run_pyquil():
    print('pyquil')

ot=OpenToplevels()
