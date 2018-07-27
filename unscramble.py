#!/usr/bin/env python3

import numpy as numpty
from projectq import MainEngine
from projectq.ops import X, H, All, Measure, QFT, C, T, Ph, CNOT

engine = MainEngine()
qubits = engine.allocate_qureg(5)
All(X) | qubits

QFT | qubits
engine.flush()
mapping, vector = engine.backend.cheat()
print(mapping)

# Need to take the mapping and use it
# to unscramble the order of vector.
# mapping is a dictionary whose keys are
# indices of qubits in the qureg and whose
# values are the indices of the bits to
# which they correspond:
#
#    qureg = | a b c d e > 
#    indices   0 1 2 3 4
#
# All indices are little-endian which
# means that the lowest index corresponds
# to the most significant bit or qubit.
#
# In this case, vector will contain
# 2^5 = 32 elements. The index of an
# element in this vector is given by
#
# k = 16 * k0 + 8 * k1 + 4 * k2 + 2 * k3 + k4
#
# where k0, k1, k2, k3, k4 are 0 or 1 and
# form a little-endian binary representation
# of the index. In other words the index can
# be expressed as k0k1k2k3k4 in binary.
#
# The dictionary mapping looks like this
#
#    0: s_0    LSB
#    1: s_1
#    2: s_2
#    3: s_3
#    4: s_4    MSB
#
# and means that the index 0 in the qureg
# conrresponds to index a in vector. Therefore
# the index k can be encoded in an array:
#
# r = [s_0,s_1,s_2,s_3,s_4]
#     LSB               MSB
#
# Then the k index can be constructed as
# 
# k = 16 * r[4] + 8 * r[3] + 4 * r[2] + 2 * r[1] + r[0]
#
# For clarity: this k corresponds to the
# location of the amplitude of the
# | > 
#
# Steps:
#
# 1) Make a complex vector of zeros to
#    be filled with the new vector of
#    amplitudes. The 
#    

print("\nwf_E is: \n\n\t",wf_E, "\n\n")
print("python array index 0:", wf_E[0])
print("python array index 1:", wf_E[1])
print("python array index 2:", wf_E[2])
print("python array index 3:", wf_E[3])
print()
