import numpy as np

def deutschjosza():

    def innerprod(a,b):
        return np.dot(a,np.conj(b).T)

    # list for states
    ket=[None]*4
    # list for outcomes
    prob=[None]*4
    # projectors
    Proj=[None]*4
    
    # Gate Implementation
    H=(1/np.sqrt(2))*np.array([[1,1],[1,-1]]) 
    # act on two qubits
    H2=np.kron(H,H)
    # make diagonal matrix 
    U=np.diag([-1,1,-1,1])

    # State initialisation
    # column vector
    state=np.array([1,0,0,0]).reshape(4,1)
    # do H
    state=np.dot(H2,state)        
    # do U
    state=np.dot(U,state)
    # do H again
    # end with H*U*H* initial  
    state=np.dot(H2,state)

    # Measurement: defining basis
    ket0=np.array([[1],[0]])
    ket1=np.array([[0],[1]])

    
    ket[0]=np.kron(ket0,ket0)
    ket[1]=np.kron(ket0,ket1)
    ket[2]=np.kron(ket1,ket0)
    ket[3]=np.kron(ket1,ket1)

    # Measurement: defining projectors P00,P01,P10,P11
   
    for i in range(0,len(Proj)):
        Proj[i]=np.dot(ket[i],ket[i].T)
        prob[i]=np.trace(np.dot(Proj[i],innerprod(state,state)))

    #return outcome probabilities
    return prob

print(deutschjosza())
