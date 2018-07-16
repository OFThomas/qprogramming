from tkinter import *

class MakeFrame():
#frame is background color object for building buttons and text on
   
   def __init__(self,location,color,width,height,row,col,sticky, rowspan=1, columnspan=1):
       
       self.frame = Frame(location, bg=color, width=width, height=height, padx=3, pady=3)
       self.frame.grid(row=row,column=col,rowspan=rowspan,columnspan=columnspan,sticky=sticky)
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
   
   def __init__(self,location,row,col,text,fun,fcolor="blue",bcolor="white"):
        self.button = Button(location, fg=fcolor,
                             bg=bcolor,text=text,
                             width=20,relief=RAISED,
                             command=fun)
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
   
