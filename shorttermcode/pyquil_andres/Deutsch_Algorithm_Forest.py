import numpy as np
from pyquil.quil import Program
from pyquil.api import QVMConnection 
from pyquil.gates import X,Z,Y,H,I 
# Invoking and renaming
qvm=QVMConnection()
p=Program() 
# Gate implementation
p.inst(H(0),H(1)) 
# Assuming the given function give the matrix
Ufma=np.array([[-1,0,0,0],
               [0,1,0,0],
               [0,0,-1,0],
               [0,0,0,1]]); 
p.defgate("Uf",Ufma); 
p.inst(("Uf",0,1)); 
p.inst(H(0),H(1))
# Measurements
p.measure(0,0)
p.measure(1,1) 
# Running the program
cr=[] 
results=qvm.run(p,cr,4) 
print(results)
