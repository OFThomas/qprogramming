from tkinter import *
from tkinter import messagebox
from functools import partial
from shor_alg import shor
from tkinter.messagebox import showinfo
import webbrowser

class MakeFrame():
#frame is background color object for building buttons and text on
   
   def __init__(self,location,color,width,height,row,col,sticky):
               self.frame = Frame(location, bg=color, width=width, height=height, padx=3, pady=3)
               self.frame.grid(row=row,column=col,sticky=sticky)
               #this needs to update the previous frame that the object is being created on
               #so location NOT self.frame.frame
               location.rowconfigure(row, weight=1)
               location.columnconfigure(col, weight=1)
               #might also need to replace new layer...
               #self.frame.rowconfigure(row,weight=1)
               #self.frame.columnconfigure(col,weight=1)
               # NO don't do it 

# An exemplary class
## Damn straight!
class MakeButton():
   
   def __init__(self,location,row,col,text,fun):
        self.fun = fun
        self.button = Button(location, fg="blue",
                             bg="white",text=text,
                             width=20,relief=RAISED,
                             command=self.fun)
        self.button.grid(row=row,column=col)
   #function for button
   def set_fun(self,new_fun):
      self.fun = new_fun
    
   def set_text(self,new_text):
      self.button.config(text=new_text)
   #move button
   def set_position(self,row,col,sticky):
      self.button.grid(row=row,column=col,sticky=sticky)
    
   def set_color(self,foreground,background):
      self.button.config(fg=foreground,bg=background)

   # Remove the button
   def destroy(self):
      self.button.destroy()
   
        
# Class for handling user interactions in the input output area
# Takes two MakeFrame objects as arguments in the constructor.
#
class MakeIO():

   # Constructor
   # Create empty dictionaries for storing textboxes, buttons,
   # labels etc.
   def __init__(self,input,output):
      self.iframe = input.frame
      self.oframe = output.frame
      self.input = {}
      self.output = {}
      self.irow,self.orow = 0,0

   # Function which adds a new object (button, etc.) to the
   # list of inputs. It automatically keeps track of where
   # things should go by incrementing a row counter
   def add_input(self,input,label):
      self.input[label] = input
      self.input[label].grid(row=self.irow,column=0)
      self.irow = self.irow + 1
      
   def make_label(self,text,label):
      self.add_input(Label(self.iframe,text=text),label)
      self.input[label].grid(row=self.irow,column=0)
      self.irow = self.irow + 1

   def make_itextbox(self,text,cmd,label):
      self.add_input(Entry(self.iframe,bd=0),label)
      self.input[label].grid(row=1,column=0)
      self.input[label].bind("<Return>", (lambda event:cmd(self.itextbox.get())))
      
   def make_input_box(self,text,cmd):
      self.make_label(text,"input_label")
      self.btn = MakeButton(self.iframe,2,0,"Submit",lambda:cmd(self.itextbox.get()))
      
   def get_answer(self):
      return self.itextbox.get()
      
   def set_output(self,text):
      self.olabel = Message(self.oframe, text=text)
      self.olabel.grid(row=0,column=0)

   def clear_all(self):
      self.ilabel.destroy()
      self.ilabel1.destroy()
      self.itextbox.destroy()
      self.btn.destroy()
      self.olabel.destroy()
