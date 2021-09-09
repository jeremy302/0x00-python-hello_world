#!/usr/bin/python3
from sys import argv

argc = len(argv) - 1
if __name__ == '__main__':
    print('{:d} argument{:s}'.format(argc, ':' if argc == 1
                                     else 's:' if argc > 1 else 's.'))
    for i in range(1, argc + 1):
        print('{:d}: {:s}'.format(i, argv[i]))
