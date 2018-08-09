#!/usr/bin/env python3
# Import the QISKit SDK
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, register

# Set your API Token and credentials.
# You can get it from https://quantumexperience.ng.bluemix.net/qx/account,
# looking for "Personal Access Token" section.
QX_TOKEN = "cbe4383360f3377fca9c27b779e77981cd92a59faca80d9c8e86f7d3229732f403a9632ad6d1ddebe76f722ac705fb37771c87e8e18f9c2ce91d41d29fd81b65"
QX_URL = "https://quantumexperience.ng.bluemix.net/api"
QX_HUB = "MY_HUB"
QX_GROUP = "MY_GROUP"
QX_PROJECT = "MY_PROJECT"

# Authenticate with the IBM Q API in order to use online devices.
# You need the API Token and the QX URL.
register(QX_TOKEN, QX_URL,
         hub=QX_HUB,
         group=QX_GROUP,
         project=QX_PROJECT)

# Create a Quantum Register with 2 qubits.
q = QuantumRegister(2)
# Create a Classical Register with 2 bits.
c = ClassicalRegister(2)
# Create a Quantum Circuit
qc = QuantumCircuit(q, c)

# Add a H gate on qubit 0, putting this qubit in superposition.
qc.h(q[0])
# Add a CX (CNOT) gate on control qubit 0 and target qubit 1, putting
# the qubits in a Bell state.
qc.cx(q[0], q[1])
# Add a Measure gate to see the state.
qc.measure(q, c)

# Compile and run the Quantum Program on a real device backend
job_exp = execute(qc, 'ibmqx4', shots=1024, max_credits=10)
result = job_exp.result()

# Show the results
print(result)
print(result.get_data())
