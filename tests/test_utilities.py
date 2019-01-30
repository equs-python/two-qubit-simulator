"""
# test_utilities.py
Test the functions in the utilities module
"""
import numpy as np
from two_qubit_simulator import conjugate_transpose

def test_conjugate_transpose():
    # Test with real-valued array
    test_array_1 = np.array([[1, 2], [3, 4]])
    assert np.allclose(
        conjugate_transpose(test_array_1),
        np.array([[1, 3], [2, 4]])
    )
    # Test with complex-valued array
    test_array_1 = np.array([[1j, 2], [1j, 4]])
    assert np.allclose(
        conjugate_transpose(test_array_1),
        np.array([[-1j, -1j], [2, 4]])
    )
