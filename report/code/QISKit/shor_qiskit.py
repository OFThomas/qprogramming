import numpy as np
import math

from math import gcd
from fractions import Fraction

from qiskit import ClassicalRegister, QuantumRegister, QuantumCircuit
from qiskit import available_backends, execute

def shor(N):
    
    # Check if number is even
    if N % 2 == 0:
        print('Even number.')
        return 2  
     
    # Step 1: Chose 1 < a < N uniformly at random
    a = np.random.randint(2,N)
    print ('Random number:', a)
    
    # Step 2: Compute b = gcd(a,N). If b > 1, output b and stop
    b = gcd(a,N)
    if b > 1:
        print('Factor found by guessing:', b)
        return b
    
    # Step 3: Find the order r of a modulo N for f(x) = a^x mod N
    # Quantum Part: using approximate periodicity to find r
    m = int(np.ceil(np.log2(N**2)))   # Size of first register
    M = 2**m   # M is the smallest power of 2 greater than N^2
    n = int(np.ceil(np.log2(N-1)))   # Size of second register - need to represent 0 to N-1
    
    # Check simulation backends
    print("Local backends: ", available_backends({'local': True}))

    # Set up quantum registers in QISKit
    reg_1 = QuantumRegister(n)
    reg_2 = QuantumRegister(m)
    reg_3 = ClassicalRegister(n)
    reg_4 = ClassicalRegister(m)
    
    # Set up quantum circuits
    circ_1 = QuantumCircuit(reg_1, reg_3)
    circ_2 = QuantumRegister(reg_2, reg_4)

    #Define the QFT on the registers
    def qft(circ, q, n):
        """n-qubit QFT on q in circ."""
        for j in range(n):
            for k in range(j):
                circ.cu1(math.pi/float(2**(j-k)), q[j], q[k])
            circ.h(q[j])
            
    #Apply the QFT to the first register
    qft(circ_1, reg_1, n)
    
    #WORKING ON A SOLUTION FOR QISKIT
    # Define the oracle O|x>|y> = |x>|y + f(x)> where + is bitwise addition
    #def f(x,y) : return (x, y^pow(a,x,N)) 
    #Apply oracle to both registers
    #Oracle(f) | (reg_1, reg_2)
    
    # Measure the second register 
    circ_2.measure(reg_3, reg_4)
    
    #Apply the QFT to the first register
    qft(circ_1, reg_1, n)
    
    # Measure the first register
    circ_1.measure(reg_1, reg_2)
    
    # Run the approximate peridicity algorithm
    engine.flush()
    
    # Determine output y of algorithm 
    y = 0
    for i in range(m):
        y = y + 2**i*int(reg_1[i])
    
    # Use continued fraction expansion of z = y/M to find r
    r = Fraction(y,M).limit_denominator(N).denominator

    # If r is odd the algorithm fails
    if r % 2 == 1:
        print('Order r found is odd: algorithm failed')
        return 0
    
    # Step 4: Find factor of N
    s = gcd(a**(r//2)-1, N)
    if s == 1 or s == N:
        print('Factor found is 1 or', N,': algorithm failed')
        return N
    
    print('Factor found by Shor\'s algorithm is', s, 'using', m+n, 'qubits')
    return s

N_input = input("Input an integer to factorise: ")
shor(int(N_input))

# Check simulation backends
print("Local backends: ", available_backends({'local': True}))

# Submit the job to the Q QASM Simulator (Up to 32 Qubits)
job_sim = execute(circ1, "local_qasm_simulator")
# Fetch result
sim_result = job_sim.result()

#Print out the simulation measuement basis and corresponding counts
print("simulation: ", sim_result)
print(sim_result.get_counts(circ1))

