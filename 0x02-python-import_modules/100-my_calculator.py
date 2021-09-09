#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == '__main__':
    argc = len(argv) - 1
    if argc != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)

    ops = {'+': add, '-': sub, '*': mul, '/': div}
    arg_a, op, arg_b = argv[1:]
    arg_a, arg_b = int(arg_a), int(arg_b)
    if op not in ops.keys():
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)

    print('{:d} {:s} {:d} = {}'.format(arg_a, op, arg_b,
                                       ops[op](arg_a, arg_b)))
