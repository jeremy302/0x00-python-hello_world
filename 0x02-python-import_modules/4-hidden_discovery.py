#!/usr/bin/python3
import sys
import hidden_4
if not (sys.version_info.major == 3 and sys.version_info.minor == 4):
    exit(1)

if __name__ == '__main__':
    for name in sorted(dir(hidden_4)):
        if not name.startswith('__'):
            print(name)
