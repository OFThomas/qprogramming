from tkinter import *
from tkinter import messagebox
from functools import partial
from shor_alg import shor
import webbrowser

class OpenToplevels(Frame):
    #open different windows
    def __init__(self):
        self.root = Tk()
        self.button_ctr=0

        hi_text="Hello World\n Do you want to do some quantum programming? \n(click me)"
        self.B0=Button(self.root, fg="white", bg="blue",text=hi_text,
                  command=self.begin)
        self.B0.grid(row=0, column=0)
        self.B1=Button(self.root, text="Project Q this way!",
                  command=run_projectq)
        self.B1.grid(row=1,column=0)
        self.B2=Button(self.root, text="Pyquil",
                  command=run_pyquil)
        self.B2.grid(row=1,column=1)
        self.B3=Button(self.root, text="qiskit",
                  command=run_qiskit)
        self.B3.grid(row=2,column=0)
        self.B4=Button(self.root, text="qsharp",
                      command=run_qsharp)
        self.B4.grid(row=2,column=1)
        self.B5=Button(self.root, text="shor",
                       command=lambda:self.change_text(self.B4,"New text"))
        self.B5.grid(row=3,column=0)
        self.B6=Button(self.root, text="Exit Tkinter", bg="red",
                  command=self.root.quit).grid(row=100, column=0, sticky="we")
        
        self.root.mainloop()
        
    def begin(self):
        print("hi there, everyone!")
        webbrowser.open("https://github.com/ot561/qprogramming/blob/master/report/Cohort_Project.pdf")

    def close_it(self, id):
        id.destroy()

    #def do_it():
        
        
    def change_text(self,button,new_text):
        button.config(text=new_text)

def run_shor():
    shor(15)
        
def run_projectq():
    print('Pq')

def run_qsharp():
    print('NO Q# for you')

def run_qiskit():
    print('qiskit')

def run_pyquil():
    print('pyquil')

ot=OpenToplevels()
