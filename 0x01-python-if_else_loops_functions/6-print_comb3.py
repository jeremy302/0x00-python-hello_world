#!/usr/bin/python3
print(', '.join([', '.join('%d%d' % (i, j) for j in range(10)
                           if j > i) for i in range(9)]))
