from tkinter import *

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
   # Just delete the object and have this as part of
   # the destructor. Is there a delete keyword in
   # python?
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
      
   def make_label(self,text,label):
      self.input[label] = Label(self.iframe,text=text)
      self.input[label].grid(row=self.irow,column=0)
      self.irow = self.irow + 1

   def make_text_entry(self,label,cmd):
      self.input[label] = Entry(self.iframe,bd=0)
      self.input[label].grid(row=self.irow,column=0)
      self.input[label].bind("<Return>",cmd)
      self.irow = self.irow + 1
                             
   def make_button(self,label,cmd):
      self.input[label] = MakeButton(self.iframe,2,0,"Submit",cmd)
      self.input[label].button.grid(row=self.irow,column=0)
      self.irow = self.irow + 1
                                         
   def make_input_box(self,text,cmd):
      self.make_label(text,"input_label")
      ## need to do lambda event: ... for binds
      self.make_text_entry("insert_box",lambda event:cmd(self.input["insert_box"].get()))
      self.make_button("insert_button",lambda:cmd(self.input["insert_box"].get()))
      
   def get_answer(self):
      return self.input["insert_box"].get()
      
   def set_output(self,text,label):
      for key in self.output:
         self.output[key].destroy()
      self.output[label] = Message(self.oframe, text=text)
      self.output[label].grid(row=self.orow,column=0)
      self.orow = self.orow + 1
      
   def clear_all(self):
      for key in self.input:
         self.input[key].destroy()
      for key in self.output:
         self.output[key].destroy()
      self.irow,self.orow = 0,0
         
   def run_function(self,fun):
      self.clear_all()
      print("What I'm about to run:",fun)
      #fun()
