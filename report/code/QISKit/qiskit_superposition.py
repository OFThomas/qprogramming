# Program written using QISKit to demonstrate the way in which to create an equal weighted
# superposition of states in the computational basis, and then simulate the measurement 
# on IBM's Q QASM simulator

# Import relevant library functions from QISKit
from qiskit import ClassicalRegister, QuantumRegister, QuantumCircuit
from qiskit import available_backends, execute

# Initiate quantum registers for gate execution, and classical registers for measurements
q = QuantumRegister(1)
c = ClassicalRegister(1)
qc = QuantumCircuit(q, c)

# Preform a Hadamard on the qubit in the quantum register to create a superposition
qc.h(q[0])
# Measure the superposition
qc.measure(q, c)

# Check simulation backends
print("Local backends: ", available_backends({'local': True}))

# Submit the job to the Q QASM Simulator (Up to 32 Qubits)
job_sim = execute(qc, "local_qasm_simulator")
# Fetch result
sim_result = job_sim.result()

#Print out the simulation measuement basis and corresponding counts
print("simulation: ", sim_result)
print(sim_result.get_counts(qc))

