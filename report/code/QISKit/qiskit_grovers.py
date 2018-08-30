# Program written using QISKit to demonstrate the way in which to implement Grovers search 
# algorithm and then simulate the measurement on IBM's Q QASM simulator

from qiskit import ClassicalRegister, QuantumRegister, QuantumCircuit, QuantumProgram
from qiskit import available_backends, execute
import numpy as np

def grover(marked_element):
	
    # Determine the number of qubits needed
    n = len(marked_element)
    N = 2**n
    print('Number of Qubits required is', n)
    print('Number of Ancillas required is', n)
    
    # Flip bitstring
    marked_element = marked_element[::-1]
    
    # Check if we can simulate on our local simulator (QASM Local simulator has 32 
    # qubits)
    if n > 32:
      print('Number of qubits required =', n, 'which is too large to simulate.')
      return 0
    
    # Determine the number of times to iterate 
    T = int(round(np.pi*np.sqrt(N)/4 - 0.5)) 
    print('Number of iterations T =',T)

    # Initialise n qubit register, classical readout register and ancilla qubit
    q = QuantumRegister(n, 'ctrl')
    c = ClassicalRegister(n+1, 'meas')
    a = QuantumRegister(n-1, 'anc')
    t = QuantumRegister(1, 'tgt')
    
    # Combine resources into a quantum circuit
    qc = QuantumCircuit(q, a, t, c)

    # Step 1: Start in an equal weihted superposition state on the quantum register 
    for i in range(n):
      qc.h(q[i])
    
    # Put the ancilla qubit into the - state
    qc.x(a[0])
    qc.h(a[0])
    
    # Step 2: Repeat applications of U_f and D
    for i in range(T):
      # Apply U_f 
      for j in range(n):
        if marked_element[j] == '0':
          qc.x(q[j])	
      
      # Implement an n-qubit CNOT gate
      qc.ccx(q[0], q[1], a[0])
      for i in range(2, n):
        qc.ccx(q[i], a[i-2], a[i-1])
      # Copy
      qc.cx(a[n-2], t[0])
      # Uncompute
      for i in range(n-1, 1, -1):
        qc.ccx(q[i], a[i-2], a[i-1])
      qc.ccx(q[0], q[1], a[0])
      
      for j in range(n):
        if marked_element[j] == '0':
          qc.x(q[j])
      
      # Apply H
      for j in range(n):
        qc.h(q[j])
        qc.x(q[j])
      
      # Apply U_0
      # Implement an n-qubit CNOT gate
      qc.ccx(q[0], q[1], a[0])
      for i in range(2, n):
        qc.ccx(q[i], a[i-2], a[i-1])
                  # Copy
      qc.cx(a[n-2], t[0])
                  # Uncompute
      for i in range(n-1, 1, -1):
        qc.ccx(q[i], a[i-2], a[i-1])
      qc.ccx(q[0], q[1], a[0])
      
      # Apply H
      for j in range(n):
        qc.x(q[j])
        qc.h(q[j])
    
      # Measure our quantum register via our classical register
      for i in range(n):
        qc.measure(q[i], c[i])

      # Execute the quantum circuit on the local simulator
      job = execute(qc, 'local_qasm_simulator')
      result = job.result()
      print('The results of the simulation shots are:', result.get_counts(qc))

# Define input type for def
str_input = input("Input a bit string to find: ")
grover(str_input) 
