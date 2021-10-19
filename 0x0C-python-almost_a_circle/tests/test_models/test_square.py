#!/usr/bin/python3
''' testing module '''
from unittest import TestCase
import io
import contextlib

Base = __import__('models.base').base.Base
Rectangle = __import__('models.rectangle').rectangle.Rectangle
Square = __import__('models.square').square.Square


class TestSquare(TestCase):
    ''' Square tests class '''
    def test_10(self):
        ''' task 10 tests '''
        self.assertTrue(issubclass(Square, Rectangle))

        r1 = Rectangle(1, 2)
        s1 = Square(1)
        self.assertEqual(s1.id, r1.id + 1)
        self.assertEqual(s1.width, 1)
        self.assertEqual(s1.height, 1)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

        s1 = Square(1, 2)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 0)

        s1 = Square(5, 2, 3, 4)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)
        self.assertEqual(s1.id, 4)

        s1 = Square(1)
        self.assertEqual(str(s1), '[Square] ({}) 0/0 - 1'.format(s1.id))
        self.assertEqual(str(Square(15, 2, 3, 4)), '[Square] (4) 2/3 - 15')

        with io.StringIO() as stout:
            with contextlib.redirect_stdout(stout):
                Square(1, 0, 0).display()
            self.assertEqual(stout.getvalue(), '#\n')

        with io.StringIO() as stout:
            with contextlib.redirect_stdout(stout):
                Square(3, 1, 1).display()
            self.assertEqual(stout.getvalue(), '\n ###\n ###\n ###\n')

        with io.StringIO() as stout:
            with contextlib.redirect_stdout(stout):
                Square(3, 6, 4).display()
            self.assertEqual(stout.getvalue(),
                             '\n\n\n\n      ###\n      ###\n      ###\n')

        with self.assertRaises(TypeError) as ctx:
            Square(1.0, 3, 4, 5)
        self.assertEqual(str(ctx.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as ctx:
            Square(2, '3', 4, 5)
        self.assertEqual(str(ctx.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as ctx:
            Square(2, 3, 4 + 0j, 5)
        self.assertEqual(str(ctx.exception), 'y must be an integer')

        # int args checks precedence
        with self.assertRaises(TypeError) as ctx:
            Square(1.0, 3.3, 3+0j, 5)
        self.assertEqual(str(ctx.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as ctx:
            Square(2, 3.3, 3+0j, 5)
        self.assertEqual(str(ctx.exception), 'x must be an integer')

        # width an height limit
        with self.assertRaises(ValueError) as ctx:
            Square(-1, 3, 4, 5)
        self.assertEqual(str(ctx.exception), 'width must be > 0')
        with self.assertRaises(ValueError) as ctx:
            Square(0, 3, 4, 5)
        self.assertEqual(str(ctx.exception), 'width must be > 0')
        # width and height limit precedence

        # x and y limit
        with self.assertRaises(ValueError) as ctx:
            Square(2, -3, 4, 5)
        self.assertEqual(str(ctx.exception), 'x must be >= 0')
        with self.assertRaises(ValueError) as ctx:
            Square(2, 3, -4, 5)
        self.assertEqual(str(ctx.exception), 'y must be >= 0')

        # x and y limit precedence
        with self.assertRaises(ValueError) as ctx:
            Square(2, -3, -4, 5)
        self.assertEqual(str(ctx.exception), 'x must be >= 0')

        Square(2, 0, 4, 5)
        Square(2, 1, 0, 5)
        Square(2, 0, 0, 5)

        # width and height vs x and y limit precedence
        with self.assertRaises(ValueError) as ctx:
            Square(0, -1, -1, 5)
        self.assertEqual(str(ctx.exception), 'width must be > 0')

        # arg checks
        with self.assertRaises(TypeError) as ctx:
            Square()
        self.assertEqual(str(ctx.exception), "__init__() missing 1 " +
                         "required positional argument: 'size'")

    def test_11(self):
        ''' task 11 tests '''

        s1 = Square(5)
        self.assertEqual(Square(5).size, 5)
        self.assertEqual(Square(1).size, 1)

        s1.size = 8
        self.assertEqual(s1.size, 8)

        with self.assertRaises(TypeError) as ctx:
            s1.size = 1.0
        self.assertEqual(str(ctx.exception), 'width must be an integer')
        with self.assertRaises(ValueError) as ctx:
            s1.size = 0
        self.assertEqual(str(ctx.exception), 'width must be > 0')

    def test_12(self):
        ''' task 12 tests '''
        s1 = Square(2, 3, 4, 5)
        s1.update(10)
        self.assertEqual(s1.id, 10)
        s1.update(1)
        self.assertEqual(s1.id, 1)

        s1.update(1, 2)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 2)

        s1.update(5, 7, 8)
        self.assertEqual(s1.id, 5)
        self.assertEqual(s1.size, 7)
        self.assertEqual(s1.x, 8)

        s1.update(9, 11, 12, 13)
        self.assertEqual(s1.id, 9)
        self.assertEqual(s1.size, 11)
        self.assertEqual(s1.x, 12)
        self.assertEqual(s1.y, 13)

        s1.update(9, 11, 12, 13, 15)
        self.assertEqual(s1.id, 9)
        self.assertEqual(s1.size, 11)
        self.assertEqual(s1.x, 12)
        self.assertEqual(s1.y, 13)

        with self.assertRaises(TypeError) as ctx:
            s1.update(1, 2.0)
        self.assertEqual(str(ctx.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as ctx:
            s1.update(1, 2, 'x')
        self.assertEqual(str(ctx.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as ctx:
            s1.update(1, 3, 4, 5 + 0j)
        self.assertEqual(str(ctx.exception), 'y must be an integer')

        with self.assertRaises(ValueError) as ctx:
            s1.update(1, 0)
        self.assertEqual(str(ctx.exception), 'width must be > 0')

        with self.assertRaises(ValueError) as ctx:
            s1.update(1, 4, -1)
        self.assertEqual(str(ctx.exception), 'x must be >= 0')
        with self.assertRaises(ValueError) as ctx:
            s1.update(1, 3, 4, -5)
        self.assertEqual(str(ctx.exception), 'y must be >= 0')

        with self.assertRaises(TypeError) as ctx:
            s1.update(1, 3+0j, 'x', 'y')
        self.assertEqual(str(ctx.exception), 'width must be an integer')

        s1 = Square(1, 3, 4, 5)
        s1.update(**{'id': 10})
        self.assertEqual(s1.id, 10)
        s1.update(**{'id': 1})
        self.assertEqual(s1.id, 1)

        s1.update(**{'id': 1, 'size': 2})
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 2)

        s1.update(**{'id': 5, 'size': 6, 'x': 8})
        self.assertEqual(s1.id, 5)
        self.assertEqual(s1.size, 6)
        self.assertEqual(s1.x, 8)

        s1.update(**{'id': 9, 'size': 10, 'x': 12, 'y': 13})
        self.assertEqual(s1.id, 9)
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.x, 12)
        self.assertEqual(s1.y, 13)

        s1.update(**{'id': 9, 'size': 11, 'x': 12, 'y': 13, 'z': 15})
        self.assertEqual(s1.id, 9)
        self.assertEqual(s1.size, 11)
        self.assertEqual(s1.x, 12)
        self.assertEqual(s1.y, 13)

        # check that kwargs are ignored if any arg is present
        s1.update(1, 2, **{'size': 3})
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 2)

        with self.assertRaises(TypeError) as ctx:
            s1.update(**{'id': 1, 'size': 2.0})
        self.assertEqual(str(ctx.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as ctx:
            s1.update(**{'id': 1, 'size': '3'})
        self.assertEqual(str(ctx.exception), 'width must be an integer')

        with self.assertRaises(TypeError) as ctx:
            s1.update(**{'id': 1, 'size': 4, 'x': 'x'})
        self.assertEqual(str(ctx.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as ctx:
            s1.update(**{'id': 1, 'size': 3, 'x': 4, 'y': 5 + 0j})
        self.assertEqual(str(ctx.exception), 'y must be an integer')

        with self.assertRaises(ValueError) as ctx:
            s1.update(**{'id': 1, 'size': 0})
        self.assertEqual(str(ctx.exception), 'width must be > 0')

        with self.assertRaises(ValueError) as ctx:
            s1.update(**{'id': 1, 'size': 2, 'x': -1})
        self.assertEqual(str(ctx.exception), 'x must be >= 0')
        with self.assertRaises(ValueError) as ctx:
            s1.update(**{'id': 1, 'size': 3, 'x': 4, 'y': -5})
        self.assertEqual(str(ctx.exception), 'y must be >= 0')

        with self.assertRaises(TypeError) as ctx:
            s1.update(**{'id': 1, 'size': 2 + 0j, 'x': 'x', 'y': 'y'})
        self.assertEqual(str(ctx.exception), 'width must be an integer')

    def test_14(self):
        ''' task 14 tests '''
        s1 = Square(2, 3, 4, 5)
        d1 = {'size': 2, 'x': 3, 'y': 4, 'id': 5}
        self.assertEqual(s1.to_dictionary(), d1)
        s1.id = 8
        d1['id'] = 8
        self.assertEqual(s1.to_dictionary(), d1)

        s1.update(1, 2)
        d1['id'] = 1
        d1['size'] = 2
        self.assertEqual(s1.to_dictionary(), d1)

        s1.update(**{'x': 8, 'y': 1, 'size': 4})
        d1['x'] = 8
        d1['y'] = 1
        d1['size'] = 4
        self.assertEqual(s1.to_dictionary(), d1)

        dr = s1.to_dictionary()
        s1.size = 10
        self.assertTrue(s1.to_dictionary() != dr)
        dr['size'] = 20
        self.assertTrue(s1.size != 20)
