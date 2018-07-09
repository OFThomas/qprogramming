from pyquil.quil  import Program 
from pyquil.api   import QVMConnection 
from pyquil.gates import H,PHASE
import numpy as np
# Invoking and renaming
qvm=QVMConnection()
p=Program()
# Gate implementation
p.inst(H(0))
theta=np.pi/2
p.inst(PHASE(theta,0))
# Measurement
p.measure(0,0)
p.measure(1,1)
# Running the program
cr=[]
results=qvm.run(p,cr,4)
print(results)
