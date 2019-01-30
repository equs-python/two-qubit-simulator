"""
Contains the Hadamard gate
"""

from .quantum_gate import QuantumGate
import numpy as np

class Hadamard(QuantumGate):
    """ Implements the Hadamard gate """
    def __init__(self):
        unitary_operator = 1/np.sqrt(2)*np.array([[1,1][1,-1]])
        super(Hadamard, self).__init__(unitary_operator,'H',2)

    def unitary_operator(self):
        return self.unitary_operator

    pass
    
