#!/usr/bin/env python3
from pyquil.quil import Program
from pyquil.api import QVMConnection
from pyquil.gates import X, I
from pyquilcompiler import compiletoquil

# Q in binary
bitstring = '01010001'

# Do quantum stuff now we have our bit string
qvm = QVMConnection()
prog = Program()
# make 8 individual bits for the 8 qubits

prog.inst(X(1), X(3), X(7))

for i in range(0, 8):
    prog.measure(i, i)

# store measurement outcomes, can change number of shots
results = qvm.run(prog)

#if explicitprinting == 1:
compiletoquil(prog)

print('\n#--------------------------------------------------------#')
print('# Result =', results[0])
print('#--------------------------------------------------------#')
