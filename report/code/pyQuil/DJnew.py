def DJintro(n): 
    print('There are', 2**(2**n),'Total amount of functions')
    print('There are always two Constant functions {0,1}')
    zeros=bin(0)[2:].zfill(2**n)
    ones=bin(2**(2**n)-1)[2:].zfill(2**n)
    input("We are now going to list the Constant and Balanced Functions. Press Enter to continue...")
    print('Enter 0 for Constant function:',zeros)
    print('Enter 1 for Constant function:',ones)
    functions=[]
    functions.append(zeros)
    functions.append(ones)
    k=2
    for i in range(0,2**(2**n)): # running on the total amount of functions
        string=bin(i)[2:].zfill(2**n)
        summ=0
        for j in range(len(string)):
            summ=summ+int(string[j])
        if summ==2**(n-1): # directly checking if balanced
            functions.append(string)
            #print('Enter',k,'for Balanced function:',string) # Listing all Balanced functions
            k=k+1
    nf=len(functions)
    print("There are",nf-2,"Balanced functions")
    print("Plese enter a number between",2,"and",nf-1,'if you want to choose any of these functions')
    choice = int(input('Please choose one of these previous functions: '))
    f=functions[choice]
    print("The function you chose is:",functions[choice])
    return f

import numpy as np
from pyquil.quil import Program
from pyquil.api import QVMConnection 
from pyquil.gates import X,Z,Y,H,I 
# Give the user the list of functions
input("This is the Deutsch-Jozsa Algorithm. Please press Enter to continue...")
n = int(input('Please enter the value n (less than 28):'))
#f=input("Please input function (as a string of 2^n bits):") # either constant or balanced
f=DJintro(n) # This function goes from a set with 2**n elements to {0,1}
tn=len(f) #2^n
print('Now the DJ algorithm will determine whether the input function is Balanced or Constant\n')
input("We are now going to run the DJ algorithm. Press Enter to continue...")
# Invoking and renaming
qvm=QVMConnection()
p=Program() 
# Applying a first round of n Hadamards
for ii in range(0, n, 1):
    p.inst(H(ii))
# Assuming the given function gives the matrix
vec=np.ones((2**n,), dtype=np.int)
for i in range(tn):
    vec[i]=vec[i]*(-1)**int(f[i])
Ufmaa=np.diag(vec)
# Defining 
p.defgate("Uf",Ufmaa); 
p.inst(("Uf",)+tuple(range(n))); 
# Applying second run of n Hadamards
for ii in range(0, n, 1):
    p.inst(H(ii))
# Measurements 
for ii in range(0, n, 1):
    p.measure(ii,ii)
# Running the program
cr=[] 
results=qvm.run(p,cr,4) 
check=results[0]
if 1 in results[0]: # checking from a single shot measurement
    print("The function that you entered is a Balanced function")
else:
    print("The function that you entered is a Constant function")

