import numpy as np
from math import gcd
from fractions import Fraction

from projectq import MainEngine
from projectq.ops import All, Measure, QFT, BasicMathGate, Deallocate, H, C, R, Swap

import matplotlib.pyplot as plt
from sys import exit
from scipy import fft

def qft(qubits):
    n = len(qubits)
    for i in reversed(range(n)):
        H | qubits[i]
        for d in range(1,i+1):
            C(R(np.pi/(2**d))) | (qubits[i-d], qubits[i])
    for i in range(int(n/2)):
        Swap | (qubits[i], qubits[n-i-1])  


def shor(N):
    # Check if number is even
    if N % 2 == 0:
        print('Even number.')
        return 2  
     
    # Step 1: Chose 1 < a < N uniformly at random
    a = np.random.randint(2,N)
    #a = 11
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

    # Check we can simulate on our local simulator
    if m + n > 28:   # 28 qubits = 4GB of RAM
        print('Number of qubits required =', m+n, 'which is too large to simulate.')
        return 0

    engine = MainEngine()
    # Initialise registers
    reg_1 = engine.allocate_qureg(m)
    reg_2 = engine.allocate_qureg(n)

    # Apply QFT to first register 
    All(H) | reg_1

    # Define the oracle O_f|x>|y> = |x>|y + f(x)> where + is bitwise XOR
    def O_f(x,y) : return (x, y^pow(a,x,N)) 
    # Apply oracle to both registers
    BasicMathGate(O_f) | (reg_1, reg_2)
    
    # Measure the second register 
    All(Measure) | reg_2
    engine.flush()
    y = 0    
    for i in range(n):
        y = y + 2**i*int(reg_2[i])
        Deallocate | reg_2[i]
        #engine.deallocate_qubit(reg_2[i])
    print(y)
    engine.flush()
    mapping, wavefunction = engine.backend.cheat()
    #print(wavefunction)
#    plt.plot(abs(np.asarray(wavefunction)), '.')
#    plt.show()
    
    fft_wf = fft(wavefunction)
    plt.plot(abs(fft_wf))
    plt.title('FFT')
    plt.show()
    
    # Apply the QFT to the first register
    QFT | reg_1
    for i in range(int(m/2)):
        Swap | (reg_1[i], reg_1[m-i-1])
    #qft(reg_1)

    engine.flush()
    mapping, wavefunction = engine.backend.cheat()
    #print(wavefunction)
    d = np.nonzero(wavefunction)
    print(d)
    plt.plot(abs(np.asarray(wavefunction)))
    plt.title('QFT')
    plt.show()
    
#    wavefunction_reg2 = np.zeros(16)
#    for k in range(16) :
#        #wavefunction_reg2[k] = np.sum(wavefunction[256*k: 256*k+255])
#        for i in range(256) : wavefunction_reg2[k] += wavefunction[256*k + i]
#
#    wavefunction_reg1 = np.zeros(256)
#    for k in range(256) :
#        for i in range(i) : wavefunction_reg1[k] += wavefunction[k + 16*i]
#
#    plt.plot(wavefunction_reg2, '.')
#    plt.show()
    # Measure the first register
    All(Measure) | reg_1
    
    # Run the approximate peridicity algorithm
    engine.flush()
    
    # Determine output y of algorithm 
    y = 0
    for i in range(m):
        y = y + 2**i*int(reg_1[i])
    
    # Use continued fraction expansion of z = y/M to find r
    r = Fraction(y,M).limit_denominator(N).denominator
    print(y, r)

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




