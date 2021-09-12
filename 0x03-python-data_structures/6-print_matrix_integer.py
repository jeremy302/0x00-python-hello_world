#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        print('{:s}'.format(
            ' '.join('{:d}'.format(cell) for cell in row)))
