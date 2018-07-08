import webbrowser
from tkinter import *
from tkinter.messagebox import showinfo

from shor_projectq import shor


def run_shor(n):
    x = shor(n)
    return x[0]


def run_projectq(flag):
    if flag == 0:
        print('Project Q DOCS here')
        webbrowser.open('https://github.com/ProjectQ-Framework/ProjectQ')
    elif flag == 1:
        s = "project q in progress"
        showinfo(title="reply", message="not implemented %s yet!" % (s))
        print(s)
    else:
        print('error')


def run_qsharp(flag):
    if flag == 0:
        print('Q # DOCS here')
        webbrowser.open(
            'https://docs.microsoft.com/en-us/quantum/quantum-qr-intro?view=qsharp-preview'
        )
    elif flag == 1:
        s = "q# NO"
        showinfo(title="reply", message="not implemented %s yet!" % (s))
        print(s)
    else:
        print('error')


def run_qiskit(flag):
    if flag == 0:
        print('Qiskit DOCS here')
        webbrowser.open('https://github.com/QISKit')
    elif flag == 1:
        s = "Qiskit still in progress"
        showinfo(title="reply", message="not implemented %s yet!" % (s))
        print(s)
    else:
        print('error')
    print(s)


def run_pyquil(flag):
    if flag == 0:
        print('Pyquil DOCS here')
        webbrowser.open('https://github.com/rigetticomputing')
    elif flag == 1:
        s = "Rigetti software still in progress"
        showinfo(title="reply", message="not implemented %s yet!" % (s))
        print(s)
    else:
        print('error')


def run_progguide(flag):
    if flag == 0:
        print('Guide DOCS here')
        webbrowser.open('https://github.com/ot561/qprogramming')
    elif flag == 1:
        s = "Quantum program should not have this value ever"
        showinfo(title="Error", message="NO pls don't" % (s))
        print(s)
    else:
        print("Error")
