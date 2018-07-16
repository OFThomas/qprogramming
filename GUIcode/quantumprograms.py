import webbrowser
from tkinter import *
from tkinter.messagebox import showinfo



class ProjectQ():

    class Shor():

        def run(n):
            # Method to run example alg
            # Should take an input
            # and return an output    
            x = shor(n)
            return x[0]
    
        def docs(n):
            return 0
        
    def __init__(self):
        self.docs = 'https://github.com/ProjectQ-Framework/ProjectQ'
        self.shor = Shor()

    ## Other ProjectQ algs here...

    ## Global docs
    def docs(self):
        webbrowser.open(self.docs)



class Pyquil():

   class Shor():

        def run(n):
           # Method to run example alg
           # Should take an input
           # and return an output    
           x = shor(n)
           return x[0]
    
        def docs(n):
            return 0
    
    
   class Deutsch():
        
        def run():
            return 0

   def __init__(self):
        self.docs = 'https://github.com/ProjectQ-Framework/ProjectQ'
        self.shor = Shor()

    ## Other ProjectQ algs here...

    ## Global docs
   def docs(self):
        webbrowser.open(self.docs)
    


class Qiskit():

   class Shor():

        def run(n):
           # Method to run example alg
           # Should take an input
           # and return an output    
           x = shor(n)
           return x[0]
    
        def docs(n):
            return 0
        
   def __init__(self):
        self.docs = 'https://github.com/ProjectQ-Framework/ProjectQ'
        self.shor = Shor()

    ## Other ProjectQ algs here...

    ## Global docs
   def docs(self):
        webbrowser.open(self.docs)
    


class Qsharp():

   class Shor():

        def run(n):
           # Method to run example alg
           # Should take an input
           # and return an output    
           x = shor(n)
           return x[0]
    
        def docs(n):
            return 0
        
   def __init__(self):
        self.docs = 'https://github.com/ProjectQ-Framework/ProjectQ'
        self.shor = Shor()

    ## Other ProjectQ algs here...

    ## Global docs
   def docs(self):
        webbrowser.open(self.docs)
    
