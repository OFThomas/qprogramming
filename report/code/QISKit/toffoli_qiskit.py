# Implementation of Control-Control-NOT or Toffoli in Qiskit

from qiskit import ClassicalRegister, QuantumRegister, QuantumCircuit, QuantumProgram
from qiskit import available_backends, execute
import numpy as np


# Initialise 3 qubit register and classical readout
q = QuantumRegister(3, 'ctrl')
c = ClassicalRegister(3, 'meas')

# Combine resources into a quantum circuit
qc = QuantumCircuit(q, c)

qc.ccx(q[0],q[1],q[2])

# Measure our quantum register via our classical register - will return all zeros 
# unless the control qubits are changed
for i in range(3):
  qc.measure(q[i], c[i])

# Execute the quantum circuit on the local simulator
job = execute(qc, 'local_qasm_simulator')
result = job.result()
print('The results of the simulation shots are:', result.get_counts(qc))

