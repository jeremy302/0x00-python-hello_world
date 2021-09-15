#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    r = matrix.copy()
    for row in r:
        for cell in row:
            cell = cell ** 2
