from tkinter import *
from tkinter import messagebox
from functools import partial
from shor_alg import shor
from tkinter.messagebox import showinfo
import webbrowser


class MakeFrame():

    def __init__(self,location,color,width,height,row,col):
               self.frame = Frame(location, bg=color, width=width, height=height, padx=3, pady=3)
               self.frame.grid(row=row,column=col,sticky="nsew")
               
               

# An exemplary class
class MakeButton():

    def __init__(self,location,row,col,text,fun):
        self.fun = fun
        self.button = Button(location, fg="white",
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
        print(type(self.root))
        self.root.resizable(width=TRUE,height=TRUE)
        self.root.geometry('{}x{}'.format(640,480))
        
        #get that professional font
        font=('Comic Sans MS', 15)
        self.root.option_add("*Font", font)
        
        # create all of the main containers
        # top_frame = Frame(self.root, bg='cyan', width=450, height=50, pady=3)
        self.center = MakeFrame(self.root, 'white', 200, 40,1,0)  
        self.view = MakeFrame(self.root,'black',100,100,0,0)



        
        # layout all of the main containers
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        #self.center.grid(row=1, sticky="nsew")

        # create the center widgets
        #self.center.grid_rowconfigure(0, weight=1)
        #self.center.grid_columnconfigure(0, weight=1)

        self.ctr_ltop = MakeFrame(self.center.frame,'blue',10,10,0,0)
        #self.ctr_ltop.grid(row=0, column=0, sticky="nsw")
        
        self.ctr_lmid = MakeFrame(self.center.frame,'yellow',10,10,1,0)
        #self.ctr_lmid.grid(row=1, column=0, sticky="nsw")
        
        self.ctr_lbot = MakeFrame(self.center.frame,'green',10,10,2,0)
        #self.ctr_lbot.grid(row=2,column=0, sticky="nsw")

        self.ctr_rtop = MakeFrame(self.center.frame,'orange',10,10,0,1)
        #self.ctr_rtop.grid(row=0, column=1, sticky="nsew")
        
        self.ctr_rmid = MakeFrame(self.center.frame,'cyan',10,10,1,1)
        #self.ctr_rmid.grid(row=1, column=1, sticky="nsew")
        
        self.ctr_rbot = MakeFrame(self.center.frame, 'purple',10,10,2,1)
        #self.ctr_rbot.grid(row=2,column=1, sticky="nsew")

        txtwdth=20
        
        #top

        self.B1 = MakeButton(self.ctr_ltop.frame,0,0,"Project Q this way!",run_projectq)
        self.B2 = MakeButton(self.ctr_rtop.frame,0,1,"Pyquil!",run_pyquil)
        self.B3 = MakeButton(self.ctr_lmid.frame,1,0,"Qiskit!",run_qiskit)
        self.B4 = MakeButton(self.ctr_rmid.frame,1,1,"Q#!",run_pyquil)
        self.B5 = MakeButton(self.ctr_lbot.frame,2,0,"Shor!",self.usr_input)
        self.B6 = MakeButton(self.root,100,0,"Exit Tkinter",self.root.quit)

        #self.B6 = MakeButton(self.root,100,0,"Exit Tkinter", bg="red",
        #                     command=self.root.quit).grid(row=100, column=0, columnspan=2, sticky="we")
        
        
        shorenterval=Button(self.ctr_rbot.frame, text='Shors value', width=txtwdth,
                command=self.usr_input)
        shorenterval.grid(row=2,column=1)


        self.B0=Button(self.root, fg="white", bg="blue",text="Quantum Programming Guide",width=2*txtwdth,
                  relief=RAISED,command=self.begin)
        self.B0.grid(row=90, column=0, columnspan=2, sticky="we")
        
        #exit
        self.B6=Button(self.root, text="Exit Tkinter", bg="red",
                  command=self.root.quit).grid(row=100, column=0, columnspan=2, sticky="we")

        self.button_0 = MakeButton(self.view.frame, 0,0,"Hello",lambda:print(10))
    
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
         
        l1=Label(self.root, text="Integer")
        l1.grid(row=10,column=10)
        ent=Entry(self.root, bd=5)
        ent.grid(row=10,column=11)
        def reply(name):
            #showinfo(title="Reply", message = "Hello %s!" % name)
            print(name)
            run_shor(int(name))

        ent.bind("<Return>", (lambda event: reply(ent.get())))
        btn = Button(self.root,text="Submit", command=(lambda: reply(ent.get())))
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
