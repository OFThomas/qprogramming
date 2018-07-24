from projectq import MainEngine
from projectq.ops import H, Measure

# Set up the simulator 
engine = MainEngine()
# Allocate a qubit
qubit = engine.allocate_qubit()
# Apply Hadamard gate to create superposition
H | qubit
# Measure the qubit to collapse to |0> or |1>
Measure | qubit
# Send the gates to the compiler/simulator
engine.flush()
# Display result
print('Output =', int(qubit))