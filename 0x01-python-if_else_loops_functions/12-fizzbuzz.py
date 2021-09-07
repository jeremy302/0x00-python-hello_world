#!/usr/bin/python3
def fizzbuzz():
    print(' '.join('%d%s' %
                   (i, ' FizzBuzz' if not i % 15 else ' Buzz' if not i % 5
                    else ' Fizz' if not i % 3 else '') for i in range(1, 101)), end='')
