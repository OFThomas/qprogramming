import numpy as np
from math import gcd
from fractions import Fraction

import projectq as pq
from projectq.ops import All, Measure, QFT, BasicMathGate


class Oracle(BasicMathGate):
    def __init__(self, f):    
        BasicMathGate.__init__(self, f)


def shor(N):
    count = 1  # Number of tries it took to find a factor
    prime_limit = 10  # Number of times you would like to run the algorithm before giving up
    guess = 0  # Becomes 1 if guessed by choice of a
    odd_order = 0  # Number of times the order was found to be odd
    trivial = 0  # Number of times trivial factors 1 or N are found
    too_large = 0  # Becomes 1 if too many qubits to simulate
    do_loop = 1  # Checks to see if we should do while loop
    
    # Check if number is even
    if N % 2 == 0:
        s = 2
        do_loop = 0
    
    m = int(np.ceil(np.log2(N**2)))   # Size of first register
    M = 2**m   # M is the smallest power of 2 greater than N^2
    n = int(np.ceil(np.log2(N-1)))   # Size of second register - need to represent 0 to N-1
    
    # Check how many qubits need to be simulated
    if m + n > 28:
        too_large = 1
        do_loop = 0
        s = 0
    
    # Define the oracle function
    def f(x,y): 
        return (x, y^pow(a,x,N)) 
    
    
    while (count < prime_limit and do_loop == 1):
        # Step 1: Chose 1 < a < N uniformly at random
        a = np.random.randint(2,N)
        
        # Step 2: Compute b = gcd(a,N). If b > 1, output b and stop
        b = gcd(a,N)
        if b > 1:
            guess = 1
            s = b
            break
        
        # Step 3: Find the order r of a modulo N for f(x) = a^x mod N
        # Quantum Part: using approximate periodicity to find r
        
        # Initialise ProjectQ engine    
        engine = pq.MainEngine()
        # Initialise registers
        reg_1 = engine.allocate_qureg(m)
        reg_2 = engine.allocate_qureg(n)
    
        # Apply QFT to first register 
        QFT | reg_1
    
        # Apply oracle to both registers
        Oracle(f) | (reg_1, reg_2)
        
        # Measure the second register 
        All(Measure) | reg_2
        
        # Apply the QFT to the first register
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
            # Increments fail counter and odd_order counter
            odd_order = odd_order + 1
            count = count + 1
        else:
            # Step 4: Find factor of N
            s = gcd(a**(r//2)-1, N)
            if s == 1 or s == N:
                # Increment fail counter and trivial counter
                trivial = trivial = 1
                count = count + 1
            else:
                # We have found a factor
                break

    # Algorithm has failed enough times you can say that N is prime
    if count == prime_limit:
        s = N
          
    return s, count, guess, odd_order, trivial, too_large

#N_input = input("Input an integer to factorise: ")

#factor, iterations, guess, odd_order, trivial, too_large = shor(int(N_input))
#print('Factor found =', factor)
#print('Iterations of the algorithm = ',iterations)
#print('Was it guessed = ', guess)
#print('Number of times order r was odd = ', odd_order)
#print('Number of times trivial factor 1 or N was found = ', trivial)
#print('Too large to simulate = ', too_large)


