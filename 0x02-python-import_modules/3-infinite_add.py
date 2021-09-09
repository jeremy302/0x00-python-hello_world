#!/usr/bin/python3
from sys import argv

argc = len(argv) - 1
s = 0
for i in range(1, argc + 1):
    s += int(argv[i])
if __name__ == '__main__':
    print('{:d}'.format(s))
