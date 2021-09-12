#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
  print('{:s}'.format('\n'.join((' '.join('%d' % cell for cell in row))
                                for row in matrix)))
