import numpy as np

# Gate Implementation
H=(1/np.sqrt(2))*np.array([[1,1],[1,-1]]) 
U=np.array([[-1,0,0,0],[0,1,0,0],[0,0,-1,0],[0,0,0,1]])

# State initialisation
state0=np.array([[1],[0],[0],[0]]) 
state1=np.dot(np.kron(H,H),state0)        
state2=np.dot(U,state1)
state3=np.dot(np.kron(H,H),state2)

# Measurement: defining basis
ket0=np.array([[1],[0]])
ket1=np.array([[0],[1]])

ket00=np.kron(ket0,ket0)
ket01=np.kron(ket0,ket1)
ket10=np.kron(ket1,ket0)
ket11=np.kron(ket1,ket1)

# Measurement: defining projectors P00,P01,P10,P11
P00=np.dot(ket00,ket00.T)
P01=np.dot(ket01,ket01.T)
P10=np.dot(ket10,ket10.T)
P11=np.dot(ket11,ket11.T)

# Probability of obtaining outcomes 00, 01, 10, 11
prob00=np.trace(np.dot(P00,np.dot(state3,np.conj(state3).T)))
prob01=np.trace(np.dot(P01,np.dot(state3,np.conj(state3).T)))
prob10=np.trace(np.dot(P10,np.dot(state3,np.conj(state3).T)))
prob11=np.trace(np.dot(P11,np.dot(state3,np.conj(state3).T)))

print(prob00,prob01,prob10,prob11)
