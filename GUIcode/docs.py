# docs.py
from functools import partial

from makestuff import MakeButton
from quantumprograms import (run_progguide, run_projectq, run_pyquil,
                             run_qiskit, run_qsharp)

# JS OT Bristol 2018


class Docs():
    def __init__(self, frame):
        self.frame = frame
        # documentation
        self.makedocs()
