#!/usr/bin/env python3
from qiskit import ClassicalRegister, QuantumRegister, QuantumCircuit
from qiskit import available_backends, execute, compile
#from qiskit.wrapper._wrapper import *
from IBMQuantumExperience import IBMQuantumExperience
from qiskit import backends

# Q in binary
bitstring = '01010001'

# Allocate memory
q = QuantumRegister(8)
c = ClassicalRegister(8)
qprog = QuantumCircuit(q, c)

# do X on q1, q3, q7
# recall H Z H is X
qprog.h(q[1])
qprog.z(q[1])
qprog.h(q[1])

qprog.x(q[3])
qprog.x(q[7])

# Measure
qprog.measure(q, c)

gates = "x,h"
cp = compile(qprog,"local_qasm_simulator",basis_gates=gates)
print(cp['circuits'][0]['compiled_circuit_qasm'])

# print quantum assembly code
print(qprog.qasm())

# Submit the job to the Q QASM Simulator
job_sim = execute(qprog, "local_qasm_simulator")

# Fetch result
sim_result = job_sim.result()

# Print out the simulation measurements
print("# Result =", sim_result)
print(sim_result.get_counts(qprog))
