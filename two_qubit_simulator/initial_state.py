def random_quantum_state():
 """
 Returns a random qubit state.
 The qubit will be a column vector with complex elements a+ib and c+id. 
 a,b,c and d are randomly chosen. The norm ensures the state is normalised. 
 """
 import numpy as np 
 import random
 a = random.random()
 b = random.random()
 c = random.random()
 d = random.random()
 norm = np.sqrt (( a + 1j * b) * (a - 1j * b) + (c + 1j * d) * (c - 1j * d))
 return np.array([[a + 1j * b] , [c + 1j * d] ]) / norm