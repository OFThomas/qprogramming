from tkinter import *
from tkinter import messagebox
from functools import partial
from shor_alg import shor
from tkinter.messagebox import showinfo
import webbrowser

class OpenToplevels(Frame):
    #open different windows
    
    Frame(bg="black")
    def __init__(self):
        self.root = Tk()
        frame=Frame(self.root,background="white")
        self.button_ctr=0
        font=('Comic Sans MS', 12)
        self.root.option_add("*Font", font)
        txtwdth=20
        hi_text="Do you want to do some quantum programming? \n(click me)"
        #top
        self.B0=Button(self.root, fg="white", bg="blue",text=hi_text,width=2*txtwdth,
                  relief=RAISED,command=self.begin)
        self.B0.grid(row=0, column=0, columnspan=2)
        
        self.B1=Button(self.root, text="Project Q this way!",width=txtwdth,
                  command=run_projectq)
        self.B1.grid(row=1,column=0)
        #mid
        self.B2=Button(self.root, text="Pyquil",width=txtwdth,
                  command=run_pyquil)
        self.B2.grid(row=1,column=1)
        
        self.B3=Button(self.root, text="qiskit",width=txtwdth,
                  command=run_qiskit)
        self.B3.grid(row=2,column=0)
        #bot
        self.B4=Button(self.root, text="qsharp",width=txtwdth,
                      command=run_qsharp)
        self.B4.grid(row=2,column=1)
        
        self.B5=Button(self.root, text="shor",width=txtwdth,
                       command=lambda:self.change_text(self.B4,"New text"))
        self.B5.grid(row=3,column=0)
        
        shorenterval=Button(self.root, text='Shors value', width=txtwdth,
                command=self.usr_input)
        shorenterval.grid(row=5,column=5)  
        #exit
        self.B6=Button(self.root, text="Exit Tkinter", bg="red",
                  command=self.root.quit).grid(row=100, column=0, columnspan=2, sticky="we")
        self.root.mainloop()
        
    def begin(self):
        print("hi there, everyone!")
        webbrowser.open("https://github.com/ot561/qprogramming/blob/master/report/Cohort_Project.pdf")

    def close_it(self, id):
        id.destroy()

    def usr_input(self):
        id=Toplevel(self.root)
        id.title("Enter a number to factorise")
         
        l1=Label(id, text="Integer")
        l1.grid(row=0,column=0)
        ent=Entry(id, bd=5)
        ent.grid(row=0,column=1)
        def reply(name):
            showinfo(title="Reply", message = "Hello %s!" % name)
            print(name)
            run_shor(int(name))

        ent.bind("<Return>", (lambda event: reply(ent.get())))
        btn = Button(id,text="Submit", command=(lambda: reply(ent.get())))
        btn.grid(row=1,column=0)
        
        return ent.get() 

    def change_text(self,button,new_text):
        button.config(text=new_text)

def run_shor(n):
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
