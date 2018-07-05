from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showinfo
import webbrowser
#constructors
from makestuff import *
#what the buttons actually do...
from quantumprograms import *

class OpenToplevels(Frame):
    #open different windows
    
    def __init__(self):
        # make window called self.root
        self.root = Tk()
        #dimensions of window 
        self.winwidth=640
        self.winheight=480
        #geometry 
        self.root.resizable(width=TRUE,height=TRUE)
        self.root.geometry('{}x{}'.format(self.winwidth,self.winheight))
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        
        #get that professional font
        font=('Comic Sans MS', 15)
        self.root.option_add("*Font", font)
        
        #make frames for backgrounds and splitting the widgits
        self.view = MakeFrame(self.root,'black',100,100,0,0,'nsew')
        self.input = MakeFrame(self.view.frame,'green',100,100,0,0,'nsew')
        self.output = MakeFrame(self.view.frame,'pink',100,100,0,1,'nswe')
        #here be buttons 
        self.control = MakeFrame(self.root, 'white',200, 40,1,0,'nsew')  
        self.interact = MakeIO(self.input,self.output)
        
        colors=['blue', 'yellow', 'green', 'orange', 'cyan', 'purple']
        buttontext=['Project Q', 'PyQuil', 'Qiskit', 'Q#', 'Shor','']
        halfcols=int(0.5*len(colors))
        self.ctrl= {}
        self.B={}
        for j in range(0,2):
            for i in range(0,halfcols):
                self.ctrl[i+j*halfcols]=MakeFrame(self.control.frame,colors[i+j*halfcols], 
                                                     10,10, 10+i, 10+j, 'nsew')
                self.B[i+j*halfcols]=MakeButton(self.ctrl[i+j*halfcols].frame,10+i,10+j, buttontext[i], lambda:self.interact.run_function(run_projectq))

        #can automate this 
        self.ctrl_ltop = MakeFrame(self.control.frame,'blue',10,10,0,0,'nsew')
        self.ctrl_lmid = MakeFrame(self.control.frame,'yellow',10,10,1,0,'nsew')
        self.ctrl_lbot = MakeFrame(self.control.frame,'green',10,10,2,0,'nsew')
        self.ctrl_rtop = MakeFrame(self.control.frame,'orange',10,10,0,1,'nsew')
        self.ctrl_rmid = MakeFrame(self.control.frame,'cyan',10,10,1,1,'nsew')
        self.ctrl_rbot = MakeFrame(self.control.frame,'purple',10,10,2,1,'nsew')

       

       #control buttons
        self.B1 = MakeButton(self.ctrl_ltop.frame,0,0,"Project Q this way!",
                             lambda:self.interact.run_function(run_projectq))
        self.B2 = MakeButton(self.ctrl_rtop.frame,0,0,"Pyquil!",
                             lambda:self.interact.run_function(run_projectq))
        self.B3 = MakeButton(self.ctrl_lmid.frame,0,0,"Qiskit!",
                             lambda:self.interact.run_function(run_projectq))
        self.B4 = MakeButton(self.ctrl_rmid.frame,0,0,"Q#!",
                             lambda:self.interact.run_function(run_projectq))
        self.B5 = MakeButton(self.ctrl_lbot.frame,0,0,"Shor!",
                             lambda:self.interact.run_function(self.usr_input))
        
        #GENERAL buttons exit
        self.Bdocs = MakeButton(self.root,90,0,"Quantum Programming Guide",self.begin)
        self.Bdocs.set_position(90,0,"we")
        self.Bexit = MakeButton(self.root,100,0,"Exit Tkinter",self.root.quit)
        self.Bexit.set_position(100,0,"we")
    
        self.root.mainloop()        

    def begin(self):
        print("hi there, everyone!")
        webbrowser.open("https://github.com/ot561/qprogramming/blob/master/report/Cohort_Project.pdf")

    def close_it(self, id):
        id.destroy()

    def usr_input(self):
        self.interact.clear_all()
        def do_shor(response):
            x=run_shor(int(response))
            self.interact.set_output("Shor's result: %s" % (x),"out_label")

        self.interact.make_input_box("Enter a number to factorise:",do_shor)
        self.interact.set_output("Shor's result:","out_label")

        return self.interact.get_answer()
    
    def printtogui(self):
        print()

    def change_text(self,button,new_text):
        button.button.config(text=new_text)
        showinfo(title="Reply", message = "Broken!" )
        button.button.destroy()

    def clear_io(self):
        self.interact.clear_all()


ot=OpenToplevels()
