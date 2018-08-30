import numpy as np

from pyquil.api import QVMConnection
from pyquil.quil import Program
from pyquil.gates import H


def grover(marked_element):
    # Determine number of qubits needed
    n = len(marked_element)
    N = 2**n
    no_marked = int(marked_element, 2)

    # Determine number of times to iterate
    T = int(round(np.pi * np.sqrt(N) / 4 - 0.5))
    print('Number of iterations T =', T)

    # Invoking and renaming Program and Connection
    qvm = QVMConnection()
    p = Program()

    # Step 1: Start with qubits in equal superposition
    for i in range(n):
        p.inst(H(i))

    # Defining Oracle matrices: U_0 and U_f
    U_0 = np.eye(N)
    U_0[0][0] = -1
    U_f = np.eye(N)
    U_f[no_marked][no_marked] = -1

    # Defining Oracle gates
    p.defgate("U0", U_0)
    p.defgate("Uf", U_f)

    # Step 2: Repeat applications of U_f and D
    for i in range(T):
        # Apply U_f
        p.inst(("Uf", ) + tuple(range(n)))

        # Apply D
        for j in range(n):
            p.inst(H(j))

        p.inst(("U0", ) + tuple(range(n)))

        for j in range(n):
            p.inst(H(j))

    # Step 3: Measure all the qubits and output result
    for i in range(n):
        p.measure(i)

    # Run the program
    results = qvm.run(p, list(range(n)), 1)

    print('Element found =', results[0])
    return results[0]


str_input = str(input("Input a bit string to find: "))
grover(str_input)
