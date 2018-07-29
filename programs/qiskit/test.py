# RUN WITH PYTHON 3.5!
# Import the Qiskit SDK
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, QuantumProgram
from qiskit import available_backends, execute
from qiskit.tools.visualization import circuit_drawer

# initialise quantum program
qp = QuantumProgram()

# Create a qubyte, Quantum Register with 8 qubits.
qbyte = qp.create_quantum_register('q1', 8)
cbyte = qp.create_classical_register('c1', 8)

:q
:q
:wq
# Create a Quantum Circuit
qc = qp.create_circuit('helloworld', [qbyte], [cbyte])

# Add a H gate on qubit 0, putting this qubit in superposition.
#qc.h(q[1])
#qc.h(q[2])
# Add a CX (CNOT) gate on control qubit 0 and target qubit 1, putting
# the qubits in a Bell state.
#qc.cx(q[0], q[1])

# Measure
for i in range(0, 8):
    qc.measure(qbyte[i], cbyte[i])

print(qp.get_qasm('helloworld'))
"""
# See a list of available local simulators
print("Local backends: ", available_backends({'local': True}))

# Compile and run the Quantum circuit on a simulator backend
job_sim = execute(qc, "local_qasm_simulator")
sim_result = job_sim.result()

# Show the results
print("simulation: ", sim_result)
print(sim_result.get_counts(qc))

# Draw the circuit
#circuit_drawer(qc, filename='./test_circuit.png')
#diagram = circuit_drawer(qc)
#diagram.show()

# print QASM

print(qp.get_asm())
"""
