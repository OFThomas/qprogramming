#!/usr/bin/env python3

from projectq import MainEngine
from projectq.ops import X, Z, H, All, Measure
from projectq.backends import CommandPrinter, Simulator
from projectq.setups import restrictedgateset
from projectq.ops import All, H, Measure, Rx, Ry, Rz, CNOT

# set restricted gate-set
restricted_list = restrictedgateset.get_engine_list(
    one_qubit_gates=(Rz, Ry), two_qubit_gates=(CNOT), other_gates=())

# set engine
restricted_compiler = MainEngine(
    backend=CommandPrinter(accept_input=False), engine_list=restricted_list)

#  compiler
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
# run for restricted gate-set
qprogram(restricted_compiler)

# then simulate
qprogram(simulate)
