#!/usr/bin/python3
'''This modules contains a function to divide matrices

Example:
matrix_divided([[1]], 1) -> [[1]]
'''


def matrix_divided(matrix, div):
    ''' divides a matrix by a scaler

    if the divisor is 0, a ZeroDivisionError is thrown.
    The matrix can't be empty

    Args:
        matrix (list): a matrix
        div (int): a number
    '''
    if (type(matrix) is not list or len(matrix) == 0 or
        any(type(row) is not list or len(row) == 0 or
            any(type(cell) not in [int, float]
                for cell in row) for row in matrix)):
        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(cell/div, 2) for cell in row] for row in matrix]
