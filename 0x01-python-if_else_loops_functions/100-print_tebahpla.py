#!/usr/bin/python3
lower = True
for i in range(25, -1, -1):
    print(chr(i + (ord('a') if lower else ord('A'))), end='')
    lower = not lower
