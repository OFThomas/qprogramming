#!/usr/bin/env python3

from projectq.backends import CommandPrinter
from projectq.backends import Simulator
from projectq.setups.default import get_engine_list
from projectq.setups import restrictedgateset
from projectq import MainEngine
from projectq.ops import X, Y, Z, Rz, Ry, CNOT, All, Measure

#eng = MainEngine(backend=CommandPrinter(accept_input=False))

#engines = get_engine_list() + [CommandPrinter()]
#eng = MainEngine(backend=Simulator(),engine_list=engines)

engines = restrictedgateset.get_engine_list(one_qubit_gates=(Rz,Ry),
                                            two_qubit_gates=(CNOT,))
eng = MainEngine(backend=CommandPrinter(accept_input=False),
                 engine_list=engines)


q = eng.allocate_qureg(4)
X | q[0]
Y | q[1]
Z | q[2]
CNOT | (q[2], q[3])
Measure | q[2]

eng.flush()
