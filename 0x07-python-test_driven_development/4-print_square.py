#!/usr/bin/python3
'''This modules contains a function to print a square

Example:
print_square(1) -> #
'''


def print_square(size):
    ''' prints a square with dimentions `size`

    A square of dimensions: `size` * `size` is printed.
    `size` must be an integer

    Args:
        size (int): side length of the square
    '''
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    print('{:s}'.format((('#' * size + '\n') * size)[0:-1]))
