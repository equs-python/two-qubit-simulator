"""
# utilities.py
Contains utility functions for the two_qubit_simulator module
"""
import numpy as np

def conjugate_transpose(array):
    """ Calculates the conjugate transpose of an array

        Parameters
        -------
        array : numpy ndarray
            The array to be transposed
        
        Returns
        -------
        numpy ndarray
            The conjugate transpose of the input array
    """
    return np.conjugate(
        np.transpose(array)
    )