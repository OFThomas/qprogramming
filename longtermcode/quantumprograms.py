import webbrowser
from tkinter import *
from tkinter.messagebox import showinfo
from shor_projectq import shor

# Contains:
#   Shor
#   DJ
#   ...
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
    
