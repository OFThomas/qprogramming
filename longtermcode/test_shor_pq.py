import numpy as np
from math import gcd
from fractions import Fraction
from random import randint

import projectq as pq
from projectq.ops import All, Measure, QFT, BasicMathGate

class Oracle(BasicMathGate):
    def __init__(self, f):    
        BasicMathGate.__init__(self, f)
        

def shor(N):
    # Check if number is even
    if N % 2 == 0:
        print('Even number. Couldn\'t you have figured that out yourself?')
        return 2  
     
    # Step 1: Chose 1 < a < N uniformly at random
    a = np.random.randint(2,N-1)
    
    # Step 2: Compute b = gcd(a,N). If b > 1, output b and stop
    b = gcd(a,N)
    if b > 1:
        print('Factor found by guessing: {0:d}'.format(b))
        return b
    
    # Step 3: Find the order r of a modulo N for f(x) = a^x mod N
    # Quantum Part: using approximate periodicity to find r
    
    m = int(np.ceil(np.log2(N**2)))   # Size of first register
    M = 2**m   # M is the smallest power of 2 greater than N^2
    n = int(np.ceil(np.log2(N-1)))   # Size of second register - need to represent 0 to N-1
    
    # Check we can simulate on our local simulator
    # FIX THIS IF STATEMENT TO LIST WHAT THE COMPANIES HAVE
    if m + n > 28:   # 28 qubits = 4GB of RAM
        print('Number of qubits required = ' + str(m+n) + '. Did you really think python could simulate that?')
        if m + n > 72 : print('Google only has 72! You need to phone DWave')
        elif m + n > 50 : print('Intel has only managed 50 qubits')
        elif m + n > 20 : print('Rigetti would have had 20 but one of them broke')
        return 0

    engine = pq.MainEngine()
    # Initialise reqgisters
    reg_1 = engine.allocate_qureg(m)
    reg_2 = engine.allocate_qureg(n)

    # Apply QFT to first register (first m qubits)
    QFT | reg_1

    # Apply oracle to both registers
    def f(x,y) : return (x, y^pow(a,x,N)) 
    Oracle(f) | (reg_1, reg_2)
    
    # Measure the second register (last n qubits)
    All(Measure) | reg_2
    
    # Apply the qft to the first register
    QFT | reg_1
    
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

    # If r is odd the algorithm fails
    if r % 2 == 1:
        print('Order r found is odd: algorithm failed')
        return 0
    
    # Step 4: Find factor of N
    s = gcd(a**(r//2)-1, N)
    if s == 1 or s == N:
        print('Factor found is 1 or', N,': algorithm failed')
        return 0
    
    print('Factor found by Shor\'s algorithm is', s, 'using',m+n, 'qubits')
    return s


count = 0

print("\n=======================================")
print("Welcome to ProjectQ -- the home of ")
print("innefectual quantum computer simulation")
print("in python! Here is an implementation of")
print("Shor's algorithm for factorising an")
print("integer. We challenge you to find one")
print("you couldn't have factorised yourself!")
print("========================================\n")

motivational_messages = ("It's not that hard mate.",
                         "Shor would be unimpressed.",
                         "Do you even know what an integer is?",
                         "Who taught you maths?",
                         "Maybe come back tomorrow.")
while(1==1):
    N_input = input("Input an integer to factorise: ")
    count = count + 1
    try:
        if int(N_input) > 1:
            if(count > 3) : print("Finally!")
            break
        else:
            print("Put in a positive number you fool. Try again.")
    except ValueError:
        print("Put in an integer you fool.",N_input,"is not a integer. Try again.")
    if count > 3 : print(motivational_messages[randint(0,4)])
shor(int(N_input))




