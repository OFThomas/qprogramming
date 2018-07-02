from tkinter import *
from tkinter import messagebox
from functools import partial
from tkinter.messagebox import showinfo
from shor_alg import shor
import webbrowser

class OpenToplevels(Frame):
    #open different windows
    def __init__(self):
        # self.shor = shor
        self.root = Tk()
        self.button_ctr=0
        button = None
        self.main_menu()
        self.root.mainloop()

    def main_menu(self):
        hi_text="Hello World\n Do you want to do some quantum programming? \n(click me)"
        hi_there=Button(self.root, fg="white", bg="blue",text=hi_text,
                        command=self.begin).grid(row=0, column=0)
        projectq=Button(self.root, text="Project Q this way!",
                        command=run_projectq).grid(row=1,column=0)
        pyquil=Button(self.root, text="Pyquil",
                      command=run_pyquil).grid(row=1,column=1)
        qiskit=Button(self.root, text="qiskit",
                      command=run_qiskit).grid(row=2,column=0)
        button=Button(self.root, text="qsharp",
                      command=run_qsharp).grid(row=2,column=1)
        exit_butt=Button(self.root, text="Exit Tkinter", bg="red",
                         command=self.root.quit).grid(row=100, column=0, sticky="we")

        lab=Button(self.root, text='Shors value', command=self.usr_input).grid(row=5,column=5)


    def usr_input(self):
        id=Toplevel(self.root)
        id.title("Enter a number to factorise")
        
        l1=Label(id, text="Integer")
        l1.grid(row=0,column=0)
        ent=Entry(id, bd=5)
        ent.grid(row=0,column=1)
        def reply(name):
            showinfo(title="Reply", message = "Hello %s!" % name)
        
        ent.bind("<Return>", (lambda event: reply(ent.get())))
        
        btn = Button(id,text="Submit", command=(lambda: reply(ent.get())))
        btn.pack(side=LEFT)

        '''
        id = Toplevel(self.root)

        id.title("Toplevel #%d" % (self.button_ctr))


        Button(id, text="Close Toplevel #%d" % (self.button_ctr),
                  command=partial(self.close_it, id),
                  bg="orange", width=20).grid(row=100, column=0)
        '''
        
    def begin(self):
        print("hi there, everyone!")
        webbrowser.open("https://github.com/ot561/qprogramming/blob/master/report/Cohort_Project.pdf")

    def close_it(self, id):
        id.destroy()

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
