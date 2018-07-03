from tkinter import *
from tkinter import messagebox
from functools import partial
from shor_alg import shor
from tkinter.messagebox import showinfo
import webbrowser

class MakeFrame():

    def __init__(self,location,color,width,height,row,col,sticky):
               self.frame = Frame(location, bg=color, width=width, height=height, padx=3, pady=3)
               self.frame.grid(row=row,column=col,sticky=sticky)
               self.frame.rowconfigure(0, weight=1)
               self.frame.columnconfigure(1, weight=40)
               
# An exemplary class
class MakeButton():

    def __init__(self,location,row,col,text,fun):
        self.fun = fun
        self.button = Button(location, fg="blue",
                             bg="white",text=text,
                             width=20,relief=RAISED,
                             command=self.fun)
        self.button.grid(row=row,column=col)

    def set_fun(self,new_fun):
        self.fun = new_fun

    def set_text(self,new_text):
        self.button.config(text=new_text)

    def set_position(self,row,col,sticky):
        self.button.grid(row=row,column=col,sticky=sticky)

    def set_color(self,foreground,background):
        self.button.config(fg=foreground,bg=background)

class OpenToplevels(Frame):
    #open different windows
    
    def __init__(self):
        # make window called self.root
        self.root = Tk()
        print(type(self.root))
        self.root.resizable(width=TRUE,height=TRUE)
        self.root.geometry('{}x{}'.format(640,480))
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1,uniform=1)
        
        #get that professional font
        font=('Comic Sans MS', 15)
        self.root.option_add("*Font", font)
        
        # top_frame = Frame(self.root, bg='cyan', width=450, height=50, pady=3)
        self.control = MakeFrame(self.root, 'white', 200, 40,1,0,'nsew')  
        self.view = MakeFrame(self.root,'black',100,100,0,0,'nsew')
        self.input = MakeFrame(self.view.frame,'green',100,100,0,0,'nsew')
        self.output = MakeFrame(self.view.frame,'pink',100,100,0,1,'nsew')

        self.ctrl_ltop = MakeFrame(self.control.frame,'blue',10,10,0,0,'nsew')
        self.ctrl_lmid = MakeFrame(self.control.frame,'yellow',10,10,1,0,'nsew')
        self.ctrl_lbot = MakeFrame(self.control.frame,'green',10,10,2,0,'nsew')
        self.ctrl_rtop = MakeFrame(self.control.frame,'orange',10,10,0,1,'nsew')
        self.ctrl_rmid = MakeFrame(self.control.frame,'cyan',10,10,1,1,'nsew')
        self.ctrl_rbot = MakeFrame(self.control.frame,'purple',10,10,2,1,'nsew')
        
        #top
        self.B1 = MakeButton(self.ctrl_ltop.frame,0,0,"Project Q this way!",run_projectq)
        self.B2 = MakeButton(self.ctrl_rtop.frame,0,0,"Pyquil!",run_pyquil)
        self.B3 = MakeButton(self.ctrl_lmid.frame,0,0,"Qiskit!",run_qiskit)
        self.B4 = MakeButton(self.ctrl_rmid.frame,0,0,"Q#!",run_pyquil)
        self.B5 = MakeButton(self.ctrl_lbot.frame,0,0,"Shor!",self.usr_input)
        self.B0 = MakeButton(self.root,90,0,"Quantum Programming Guide",self.begin)
        self.B0.set_position(90,0,"we")
        self.B6 = MakeButton(self.root,100,0,"Exit Tkinter",self.root.quit)
        self.B6.set_position(100,0,"we")
    
        self.root.mainloop()
        

    def makebackground(self):
        print()
        
    def begin(self):
        print("hi there, everyone!")
        webbrowser.open("https://github.com/ot561/qprogramming/blob/master/report/Cohort_Project.pdf")

    def close_it(self, id):
        id.destroy()

    def usr_input(self):
        #id=Toplevel(self.root)
        #id.title("Enter a number to factorise")
         
        l1=Label(self.view.frame, text="Integer")
        l1.grid(row=10,column=10)
        ent=Entry(self.view.frame, bd=5)
        ent.grid(row=10,column=11)
        def reply(name):
            #showinfo(title="Reply", message = "Hello %s!" % name)
            print(name)
            run_shor(int(name))

        ent.bind("<Return>", (lambda event: reply(ent.get())))
        btn = Button(self.view.frame,text="Submit", command=(lambda: reply(ent.get())))
        btn.grid(row=11,column=10)
        
        return ent.get() 

    def change_text(self,button,new_text):
        button.config(text=new_text)
        showinfo(title="Reply", message = "Broken!" )


def run_shor(n):
    shor(n)
        
def run_projectq():
    s="Project Q"
    showinfo(title="Reply", message = "Not implemented %s yet!" % (s) )
    print(s)

def run_qsharp():
    print('NO Q# for you')
    s="Q#"
    showinfo(title="Reply", message = "Not implemented %s yet!" % (s) )
    print(s)

def run_qiskit():
    s="Qiskit"
    showinfo(title="Reply", message = "Not implemented %s yet!" % (s) )
    print(s)

def run_pyquil():
    s='PyQuil'
    showinfo(title="Reply", message = "Not implemented %s yet!" % (s) )
    print(s)


ot=OpenToplevels()
