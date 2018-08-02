#!/usr/bin/env python3

from projectq import MainEngine
from projectq.ops import X, Z, H, All, Measure
from projectq.backends import CommandPrinter
from projectq.backends import Simulator

# specify compiler
compiler = MainEngine(backend=CommandPrinter(accept_input=False))
# specify simulate locally
simulate = MainEngine(backend=Simulator())


def qprogram(eng):
    q = eng.allocate_qureg(8)

    # Q in binary
    # bitstring = '01010001'

    # recall H Z H is X
    H | q[1]
    Z | q[1]
    H | q[1]

    X | q[3]
    X | q[7]

    # measure all the qubits
    All(Measure) | q

    # execute the quantum program
    eng.flush()

    # only print the results if it has been simulated
    if eng == simulate:
        results = []
        # the values of qubits is stored as the
        # integer value of the object
        for element in q:
            results.append(int(q[int(element)]))
        print(results)


# run for the compiler to see what the program does
qprogram(compiler)
# then simulate
qprogram(simulate)
