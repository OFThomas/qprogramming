from tkinter import *
from tkinter import messagebox
from functools import partial
from shor_alg import shor
from tkinter.messagebox import showinfo
import webbrowser

class OpenToplevels(Frame):
    #open different windows
    
    def __init__(self):
        # make window called self.root 
        self.root = Tk()
        self.root.resizable(width=TRUE,height=TRUE)
        self.root.geometry('{}x{}'.format(640,480))

        self.button_ctr=0
        #get that professional font
        font=('Comic Sans MS', 12)
        self.root.option_add("*Font", font)
        
        # create all of the main containers
       # top_frame = Frame(self.root, bg='cyan', width=450, height=50, pady=3)
        center = Frame(self.root, bg='white', width=50, height=40, padx=3, pady=3)
        #btm_frame = Frame(self.root, bg='white', width=450, height=45, pady=3)

        # layout all of the main containers
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        center.grid(row=1, sticky="nsew")

        # create the center widgets
        center.grid_rowconfigure(0, weight=1)
        center.grid_columnconfigure(0, weight=1)

        ctr_ltop = Frame(center, bg='blue', width=10, height=10)
        ctr_ltop.grid(row=0, column=0, sticky="nsew")
        
        ctr_lmid = Frame(center, bg='yellow', width=10, height=10, padx=3, pady=3)
        ctr_lmid.grid(row=1, column=0, sticky="nsew")
        
        ctr_lbot = Frame(center, bg='green', width=10, height=10, padx=3, pady=3)
        ctr_lbot.grid(row=2,column=0, sticky="nsew")

        ctr_rtop = Frame(center, bg='blue', width=10, height=10)
        ctr_rtop.grid(row=0, column=1, sticky="nsew")
        
        ctr_rmid = Frame(center, bg='yellow', width=10, height=10, padx=3, pady=3)
        ctr_rmid.grid(row=1, column=1, sticky="nsew")
        
        ctr_rbot = Frame(center, bg='green', width=10, height=10, padx=3, pady=3)
        ctr_rbot.grid(row=2,column=1, sticky="nsew")



        txtwdth=20

        hi_text="Do you want to do some quantum programming? \n(click me)"
        #top
        self.B0=Button(self.root, fg="white", bg="blue",text=hi_text,width=2*txtwdth,
                  relief=RAISED,command=self.begin)
        self.B0.grid(row=0, column=0, columnspan=2)
        
        self.B1=Button(center, text="Project Q this way!",width=txtwdth,
                  command=run_projectq)
        self.B1.grid(row=0,column=0)
        #mid
        self.B2=Button(center, text="Pyquil",width=txtwdth,
                  command=run_pyquil)
        self.B2.grid(row=0,column=1)
        
        self.B3=Button(center, text="Qiskit",width=txtwdth,
                  command=run_qiskit)
        self.B3.grid(row=1,column=0)
        #bot
        self.B4=Button(center, text="Q#",width=txtwdth,
                      command=run_qsharp)
        self.B4.grid(row=1,column=1)
        
        self.B5=Button(center, text="shor",width=txtwdth,
                       command=lambda:self.change_text(self.B4,"New text"))
        self.B5.grid(row=2,column=0)
        
        shorenterval=Button(center, text='Shors value', width=txtwdth,
                command=self.usr_input)
        shorenterval.grid(row=2,column=1)  
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
