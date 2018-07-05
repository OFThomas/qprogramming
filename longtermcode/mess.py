#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showinfo
import webbrowser
#what the buttons actually do...
from quantumprograms import *
#constructors
from makestuff import *

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
<<<<<<< HEAD
        # documentation
        self.docframe=MakeFrame(self.root, 'lime', 100,100,20,0,'nesw')
       
        doclabels=[['Quantum programming guide',lambda:None], 
                ['Riggeti docs',lambda:None],
                ['Qiskit docs',lambda:None],
                ['Project Q docs',lambda:None]]

        #for i in range(0,len(doclabels)):
        #    self.Bdocs[i]=MakeButton(self.docframe.frame, i,0,)

        colors=['blue', 'yellow', 'green', 'orange', 'cyan', 'purple']
        button_atr=[['Project Q',run_projectq], ['PyQuil',run_pyquil],
=======
        
        self.colors=['blue', 'yellow', 'green', 'orange', 'cyan', 'purple']
        self.button_atr=[['Project Q',run_projectq], ['PyQuil',run_pyquil],
>>>>>>> cd22168b22eec6160df3bc99e9678487e9cc2ef6
                    ['Qiskit',run_qiskit], ['Q#',run_qsharp],
                    ['Shor',run_qsharp],['something',run_projectq]]
        self.halfcols=int(0.5*len(self.colors))
        
        self.ctrl=[None]*len(self.colors)
        self.B=[None]*len(self.colors)
        
        print('\n',run_projectq)
        print(run_qsharp)
        print(run_pyquil)
        print(run_qiskit,'\n')

        for j in range(0,2):
            for i in range(0,self.halfcols):
                self.ctrl[i+j*self.halfcols]=MakeFrame(self.control.frame, self.colors[i+j*self.halfcols], 
                                                  10,10,i,j, 'nsew')
                self.B[i+j*self.halfcols]=MakeButton(self.ctrl[i+j*self.halfcols].frame, i,j,
                                        self.button_atr[i+j*self.halfcols][0],
                                        lambda:self.run_function(self.button_atr[i+j*self.halfcols][0]))
                print("In loop:",self.button_atr[i+j*self.halfcols][0], self.B[i+j*self.halfcols].fun)
                
                #self.B[i+j*halfcols].fun()
                if i+j*self.halfcols > 2 : break

        
        #print('\n frame ', self.ctrl, '\n')
        #print('type self.ctrl', type(self.ctrl), 'type self.ctrl[0]', type(self.ctrl[0]), '\n')
        #for y in range(0,len(colors)):
        #    text=self.ctrl[y]
        #    print('type self.ctrl[%d]' % (y), type(self.ctrl[y]) )
        #    print('button location', text.frame) 
        
        #print('\n button', self.B, '\n')

        print("\n\nOut of loop:",self.button_atr[0][0], self.B[0].fun)
        self.B[0].fun()
        #print(a)
        #print(a())
        print("Out of loop:",self.button_atr[1][0], self.B[1].fun)
        self.B[1].fun()
        print("Out of loop:",self.button_atr[2][0], self.B[2].fun)
        self.B[2].fun()
        print("Out of loop:",self.button_atr[3][0], self.B[3].fun)
        self.B[3].fun()
        print("Out of loop:",self.button_atr[4][0], self.B[4].fun)
        self.B[4].fun()
        print("Out of loop:",self.button_atr[5][0], self.B[5].fun)
        self.B[5].fun()
        
        print("Here is before:",type(self.button_atr[0][1]), print(self.button_atr[0][1]))
        print("What type is this:",type(run_projectq), print(run_projectq))
        
        #GENERAL buttons exit
        self.Bdocs = MakeButton(self.root,90,0,"Quantum Programming Guide",self.begin)
        self.Bdocs.set_position(90,0,"we")
        self.QPrexit = MakeButton(self.root,100,0,"Exit Tkinter",self.root.quit)
        self.QPrexit.set_position(100,0,"we")
    
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

    def run_function(self,label):
        self.interact.clear_all()
        print("What I'm about to run IN FUN:",self.button_atr(label))
        #fun()


ot=OpenToplevels()
