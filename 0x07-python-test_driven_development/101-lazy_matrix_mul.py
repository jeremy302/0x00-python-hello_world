#!/usr/bin/python3
'''This modules contains a function to multiply 2 matrices using numpy

Example:
matrix_mul([[1]], [[2]]) -> [[2]]
'''
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    ''' returns the product of 2 matrices using numpy

    2 matrices are multiplied with numpy and the result is returned.
    The matrices must be vaid and of complementing shapes.

    Args:
        m_a (list): a matrix
        m_b (list): a matrix
    '''

    return np.matmul(m_a, m_b).tolist()
