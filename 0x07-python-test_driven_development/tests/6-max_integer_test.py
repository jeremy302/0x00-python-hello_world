#!/usr/bin/python3
'''This modules contains a class to test the max_integer function

Example:
max_integer([1, 2, 3]) -> 3
'''
from unittest import TestCase

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(TestCase):
    ''' Text class for the max_integer function.
        It test positive, negative, single and empty lists.
    '''
    def test_positives(self):
        ''' tests positive integers

        checks if the biggest integer is returned
        '''
        self.assertEqual(3, max_integer([0, 1, 2, 3]))
        self.assertEqual(499422, max_integer([10, 494, 39, 499422]))
        self.assertEqual(23333333, max_integer([10000, 999, 23333333]))
        self.assertEqual(1899999999999999, max_integer([1899999999999999,
                                                        999999999999999]))

    def test_negatives(self):
        ''' tests negative integers

        checks if the biggest integer is returned
        '''
        self.assertEqual(0, max_integer([0, -1, -2, -3]))
        self.assertEqual(-10, max_integer([-10, -494, -39, -499422]))
        self.assertEqual(-999, max_integer([-10000, -999, -23333333]))
        self.assertEqual(1899999999999999, max_integer([1899999999999999,
                                                        999999999999999]))
        self.assertEqual(999999999999, max_integer([-9999999999999999,
                                                    999999999999]))

    def test_single(self):
        ''' tests single integers

        checks if the biggest integer is returned
        '''
        self.assertEqual(5, max_integer([5]))
        self.assertEqual(0, max_integer([0]))
        self.assertEqual(-10, max_integer([-10]))
        self.assertEqual(999999999999, max_integer([999999999999]))
        self.assertEqual(-999999999999, max_integer([-999999999999]))

    def test_empty(self):
        ''' tests empty integers

        checks if the biggest integer is returned

        Args:
            self (TextMaxInteger): current instance
        '''
        self.assertEqual(None, max_integer([]))
