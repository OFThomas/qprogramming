from fractions import Fraction
from math import gcd
from random import randint

import numpy as np
import projectq as pq
from projectq.ops import QFT, All, BasicMathGate, Measure


class Oracle(BasicMathGate):
    def __init__(self, f):
        BasicMathGate.__init__(self, f)


def shor(N):
    # Check if number is even
    if N % 2 == 0:
        evenstr = 'Even number. Couldn\'t you have figured that out yourself?'
        print(evenstr)
        return evenstr

    # Step 1: Chose 1 < a < N uniformly at random
    a = np.random.randint(2, N - 1)

    # Step 2: Compute b = gcd(a,N). If b > 1, output b and stop
    b = gcd(a, N)
    if b > 1:
        guessstr = 'Factor found by guessing: {0:d}'.format(b)
        print(guessstr)
        return guessstr

    # Step 3: Find the order r of a modulo N for f(x) = a^x mod N
    # Quantum Part: using approximate periodicity to find r

    m = int(np.ceil(np.log2(N**2)))  # Size of first register
    M = 2**m  # M is the smallest power of 2 greater than N^2
    n = int(np.ceil(
        np.log2(N -
                1)))  # Size of second register - need to represent 0 to N-1

    # Check we can simulate on our local simulator
    # FIX THIS IF STATEMENT TO LIST WHAT THE COMPANIES HAVE
    if m + n > 28:  # 28 qubits = 4GB of RAM
        print('Number of qubits required = ' + str(m + n) +
              '. Did you really think python could simulate that?')
        if m + n > 72: print('Google only has 72! You need to phone DWave')
        elif m + n > 50: print('Intel has only managed 50 qubits')
        elif m + n > 20:
            print('Rigetti would have had 20 but one of them broke.')
        return 'Too many qubits required'

    engine = pq.MainEngine()
    # Initialise reqgisters
    reg_1 = engine.allocate_qureg(m)
    reg_2 = engine.allocate_qureg(n)

    # Apply QFT to first register (first m qubits)
    QFT | reg_1

    # Apply oracle to both registers
    def f(x, y):
        return (x, y ^ pow(a, x, N))

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
        y = y + 2**i * int(reg_1[i])

    # Use continued fraction expansion of z = y/M to find r
    r = Fraction(y, M).limit_denominator(N).denominator

    # If r is odd the algorithm fails
    if r % 2 == 1:
        orderoddstr = 'Order r found is odd: algorithm failed'
        print(orderoddstr)
        return orderoddstr

    # Step 4: Find factor of N
    s = gcd(a**(r // 2) - 1, N)
    if s == 1 or s == N:
        nonefoundstr = 'Factor found is 1 or %d : algorithm failed' % (N)
        print(nonefoundstr)
        return nonefoundstr

    foundfactstr = "Factor found by Shor\'s algorithm is %d using %d qubits" % (
        s, m + n)
    print(foundfactstr)
    return foundfactstr
