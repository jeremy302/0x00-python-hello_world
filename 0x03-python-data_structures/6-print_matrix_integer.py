#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    print('{:s}'.format('\n'.join((' '.join('{}'.format(cell)
                                             for cell in row))
                                  for row in matrix)))
