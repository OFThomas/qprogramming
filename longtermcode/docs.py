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

    def makedocs(self):
        self.doclabels = [['Q programming guide',
                           partial(run_progguide, 0)], [
                               'Riggeti docs',
                               partial(run_pyquil, 0)
                           ], ['Qiskit docs',
                               partial(run_qiskit, 0)],
                          ['Project Q docs',
                           partial(run_projectq,
                                   0)], ['Q# docs',
                                         partial(run_qsharp, 0)]]

        # do loop
        docbutton = [None] * len(self.doclabels)
        j = 0
        i = 0
        for count in range(0, int(len(self.doclabels))):
            if i > 1:
                j += 1
                i = 0
            docbutton[count] = MakeButton(self.frame, j, i,
                                          self.doclabels[count][0],
                                          self.doclabels[count][1])
            i += 1
