#!/usr/bin/python3
'''This modules contains a function to multiply 2 matrices

Example:
matrix_mul([[1]], [[2]]) -> [[2]]
'''


def matrix_mul(m_a, m_b):
    ''' returns the product of 2 matrices

    2 matrices are multiplied and the result is returned.
    The matrices must be vaid and of complementing shapes.

    Args:
        m_a (list): a matrix
        m_b (list): a matrix
    '''
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")
    if any(type(row) is not list for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if any(type(row) is not list for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0 or all(len(row) == 0 for row in m_a):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or all(len(row) == 0 for row in m_b):
        raise ValueError("m_b can't be empty")
    if any(any(type(cell) not in [int, float] for cell in row) for row in m_a):
        raise TypeError("m_a should contain only integers or floats")
    if any(any(type(cell) not in [int, float] for cell in row) for row in m_b):
        raise TypeError("m_b should contain only integers or floats")
    if any(len(row) != len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    res = [[0 for col in m_b[0]] for row in m_a]
    for i_a in range(len(m_a)):
        row_a = m_a[i_a]
        for j_b in range(len(m_b[0])):
            s = sum(row_a[i] * m_b[i][j_b] for i in range(len(m_b)))
            res[i_a][j_b] = s
    return res
