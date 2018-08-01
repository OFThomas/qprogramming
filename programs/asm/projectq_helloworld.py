#!/usr/bin/env python3

from projectq.backends import CommandPrinter
from projectq.backends import Simulator
#from projectq.setups.default import get_engine_list
#from projectq.setups import restrictedgateset
from projectq import MainEngine
from projectq.ops import X, Y, Z, Rz, Ry, CNOT, All, Measure

# Q in binary
bitstring = '01010001'

eng = MainEngine(backend=CommandPrinter(accept_input=False))

#engines = get_engine_list() + [CommandPrinter()]
#eng = MainEngine(backend=Simulator(),engine_list=engines)

#engines = restrictedgateset.get_engine_list(one_qubit_gates=(Rz,Ry),                                            two_qubit_gates=(CNOT,))
#eng = MainEngine(backend=CommandPrinter(accept_input=False),engine_list=engines)


q = eng.allocate_qureg(8)
X | q[1]
X | q[3]
X | q[7]

for i in range(0,8):
    Measure | q[i]

eng.flush()
