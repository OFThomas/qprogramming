#!/usr/bin/env python3
from pyquil.quil import Program
from pyquil.api import QVMConnection
from pyquil.gates import X, Z, H
from pyquilcompiler import compiletoquil

# Q in binary
bitstring = '01010001'

# Do quantum stuff now we have our bit string
qvm = QVMConnection()
qprog = Program()
# make 8 individual bits for the 8 qubits

qprog.inst(H(1), Z(1), H(1))
qprog.inst(X(3))
qprog.inst(X(7))


for i in range(0, 8):
   qprog.measure(i, i)

# store measurement outcomes, can change number of shots
results = qvm.run(qprog)

#if explicitprinting == 1:
compiletoquil(qprog)

print('\n#--------------------------------------------------------#')
print('# Result =', results[0])
print('#--------------------------------------------------------#')
