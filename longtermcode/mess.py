from tkinter import *
from tkinter import messagebox
from functools import partial
from shor_alg import shor
from tkinter.messagebox import showinfo
import webbrowser


class MakeButton():

    def __init__(self,frame,row,col,text,fun):
        self.fun = fun
        self.button = Button(frame, fg="white",
                             bg="blue",text=text,
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
        self.root.resizable(width=TRUE,height=TRUE)
        self.root.geometry('{}x{}'.format(640,480))
        
        #get that professional font
        font=('Comic Sans MS', 15)
        self.root.option_add("*Font", font)
        
        # create all of the main containers
        # top_frame = Frame(self.root, bg='cyan', width=450, height=50, pady=3)
        self.center = Frame(self.root, bg='white', width=200, height=40, padx=3, pady=3)
        #btm_frame = Frame(self.root, bg='white', width=450, height=45, pady=3)

        # layout all of the main containers
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.center.grid(row=1, sticky="nsew")

        # create the center widgets
        self.center.grid_rowconfigure(0, weight=1)
        self.center.grid_columnconfigure(0, weight=1)

        self.ctr_ltop = Frame(self.center, bg='blue', width=10, height=10, padx=3, pady=3)
        self.ctr_ltop.grid(row=0, column=0, sticky="nsw")
        
        self.ctr_lmid = Frame(self.center, bg='yellow', width=10, height=10, padx=3, pady=3)
        self.ctr_lmid.grid(row=1, column=0, sticky="nsw")
        
        self.ctr_lbot = Frame(self.center, bg='green', width=10, height=10, padx=3, pady=3)
        self.ctr_lbot.grid(row=2,column=0, sticky="nsw")

        self.ctr_rtop = Frame(self.center, bg='orange', width=10, height=10, padx=3, pady=3)
        self.ctr_rtop.grid(row=0, column=1, sticky="nsew")
        
        self.ctr_rmid = Frame(self.center, bg='cyan', width=10, height=10, padx=3, pady=3)
        self.ctr_rmid.grid(row=1, column=1, sticky="nsew")
        
        self.ctr_rbot = Frame(self.center, bg='purple', width=10, height=10, padx=3, pady=3)
        self.ctr_rbot.grid(row=2,column=1, sticky="nsew")

        txtwdth=20
        
        #top

        self.B1 = MakeButton(self.ctr_ltop,0,0,"Project Q this way!",run_projectq)
        self.B2 = MakeButton(self.ctr_rtop,0,1,"Pyquil!",run_pyquil)
        self.B3 = MakeButton(self.ctr_lmid,1,0,"Qiskit!",run_qiskit)
        self.B4 = MakeButton(self.ctr_rmid,1,1,"Q#!",run_pyquil)
        self.B5 = MakeButton(self.ctr_lbot,2,0,"Shor!",run_shor)

        self.B6 = MakeButton(self.root,100,0,"Exit Tkinter",self.root.quit)

        #self.B6 = MakeButton(self.root,100,0,"Exit Tkinter", bg="red",
        #                     command=self.root.quit).grid(row=100, column=0, columnspan=2, sticky="we")
        
        
        shorenterval=Button(self.ctr_rbot, text='Shors value', width=txtwdth,
                command=self.usr_input)
        shorenterval.grid(row=2,column=1)


        self.B0=Button(self.root, fg="white", bg="blue",text="Quantum Programming Guide",width=2*txtwdth,
                  relief=RAISED,command=self.begin)
        self.B0.grid(row=90, column=0, columnspan=2, sticky="we")
        
        #exit
        self.B6=Button(self.root, text="Exit Tkinter", bg="red",
                  command=self.root.quit).grid(row=100, column=0, columnspan=2, sticky="we")

        self.button_0 = MakeButton(self.root,0,0,"Hello",lambda:print(10))
        
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
         
        l1=Label(self.center, text="Integer")
        l1.grid(row=10,column=10)
        ent=Entry(center, bd=5)
        ent.grid(row=10,column=11)
        def reply(name):
            #showinfo(title="Reply", message = "Hello %s!" % name)
            print(name)
            run_shor(int(name))

        ent.bind("<Return>", (lambda event: reply(ent.get())))
        btn = Button(center,text="Submit", command=(lambda: reply(ent.get())))
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
