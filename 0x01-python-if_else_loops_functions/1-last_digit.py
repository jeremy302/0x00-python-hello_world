#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10 if number > 0 else -(-number % 10)
range_str = 'greater than 5' if last_digit > 5\
    else '0' if last_digit == 0 else 'less than 6 and not 0'
print('Last digit of %d is %d and is %s' % (number, last_digit, range_str))
