#!/usr/bin/env python3

# Import relevant library functions from QISKit
from qiskit import ClassicalRegister, QuantumRegister, QuantumCircuit
from qiskit import available_backends, execute

# Q in binary
bitstring = '01010001'

# Allocate memory
q = QuantumRegister(8)
c = ClassicalRegister(8)
qprog = QuantumCircuit(q, c)

qprog.x(q[1])
qprog.x(q[3])
qprog.x(q[7])

# Measure the superposition
qprog.measure(q, c)

# Submit the job to the Q QASM Simulator (Up to 32 Qubits)
job_sim = execute(qprog, "local_qasm_simulator")
# Fetch result
sim_result = job_sim.result()

#Print out the simulation measuement basis and corresponding counts
print("simulation: ", sim_result)
print(sim_result.get_counts(qprog))

print(qprog.qasm())
