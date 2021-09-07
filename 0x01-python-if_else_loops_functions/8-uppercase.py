#!/usr/bin/python3
def uppercase(str):
    print(''.join([(c if c < 'a' or c > 'z'
                    else chr(ord(c) - (ord('a') - ord('A')))) for c in str]))
