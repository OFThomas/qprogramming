from tkinter import *
from tkinter.messagebox import showinfo

from shor_projectq import shor


def run_shor(n):
    x = shor(n)
    return x[0]


def run_projectq(flag):
    if flag == 0:
        print('Q # DOCS here')
    elif flag == 1:
        print('no q# for you')
        s = "q#"
        showinfo(title="reply", message="not implemented %s yet!" % (s))
        print(s)
    else:
        print('error')
    s = "project q"
    showinfo(title="reply", message="not implemented %s yet!" % (s))
    print(s)


def run_qsharp(flag):
    if flag == 0:
        print('Q # DOCS here')
    elif flag == 1:
        print('no q# for you')
        s = "q#"
        showinfo(title="reply", message="not implemented %s yet!" % (s))
        print(s)
    else:
        print('error')
    

def run_qiskit(flag):
    if flag == 0:
        print('Q # DOCS here')
    elif flag == 1:
        print('no q# for you')
        s = "q#"
        showinfo(title="reply", message="not implemented %s yet!" % (s))
        print(s)
    else:
        print('error')
    s = "qiskit"
    showinfo(title="reply", message="not implemented %s yet!" % (s))
    print(s)


def run_pyquil(flag):
    if flag == 0:
        print('Q # DOCS here')
    elif flag == 1:
        print('no q# for you')
        s = "q#"
        showinfo(title="reply", message="not implemented %s yet!" % (s))
        print(s)
    else:
        print('error')
    s = 'pyquil'
    showinfo(title="reply", message="not implemented %s yet!" % (s))
    print(s)
