#!/usr/bin/env python3

from projectq import MainEngine
from projectq.ops import X, Y, Z, Rz, Ry, All, Measure
from projectq.backends import CommandPrinter
from projectq.backends import Simulator

# Q in binary
bitstring = '01010001'

eng = MainEngine(backend=CommandPrinter(accept_input=False))

#eng = MainEngine()
#engines = get_engine_list() + [CommandPrinter()]
#eng = MainEngine(backend=Simulator(),engine_list=engines)

#engines = restrictedgateset.get_engine_list(one_qubit_gates=(Rz,Ry),                                            two_qubit_gates=(CNOT,))
#eng = MainEngine(backend=CommandPrinter(accept_input=False),engine_list=engines)

q = eng.allocate_qureg(8)

X | q[1]
X | q[3]
X | q[7]

All(Measure) | q

eng.flush()


results=[]
for element in q:
    results.append(int(q[int(element)]))
print(results)

