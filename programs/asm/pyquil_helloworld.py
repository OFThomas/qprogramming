#!/usr/bin/env python3
from pyquil.quil import Program
from pyquil.api import QVMConnection
from pyquil.gates import X, Z, H
from compile_for_pyquil import compiletoquil

# Q in binary
bitstring = '01010001'

# Do quantum stuff now we have our bit string
qvm = QVMConnection()
qprog = Program()

# do X on q1, q3, q7
# remember H Z H is X
qprog.inst(H(1), Z(1), H(1))
qprog.inst(X(3))
qprog.inst(X(7))

# do measurement over all 8 qubits
for i in range(0, 8):
    qprog.measure(i, i)

# store measurement outcomes
results = qvm.run(qprog)

# show info when compiled to 8 qubit AGAVE
compiletoquil(qprog)

print('# Result =', results[0])
