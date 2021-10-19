#!/usr/bin/python3
''' testing module '''
from unittest import TestCase
import io
import contextlib

Base = __import__('models.base').base.Base
Rectangle = __import__('models.rectangle').rectangle.Rectangle
Square = __import__('models.square').square.Square


class TestRectangle(TestCase):
    ''' Rectangle tests class '''
    def test_2(self):
        ''' task 2 tests '''
        # subsclass tests
        self.assertTrue(issubclass(Rectangle, Base))

        # right id tests
        r1 = Rectangle(1, 1)
        r2 = Rectangle(5, 5)
        self.assertEqual(r2.id - r1.id, 1)
        self.assertEqual(Rectangle(1, 2, 3, 4, 5).id, 5)
        self.assertEqual(Rectangle(1, 1).id - r2.id, 1)

        # right attributes assignments
        r3 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r3.width, 1)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 3)
        self.assertEqual(r3.y, 4)
        self.assertEqual(r3.id, 5)

        # args check
        with self.assertRaises(TypeError) as ctx:
            Rectangle()
        self.assertEqual(str(ctx.exception), "__init__() missing 2 " +
                         "required positional arguments: 'width' and 'height'")
        with self.assertRaises(TypeError) as ctx:
            Rectangle(1)
        self.assertEqual(str(ctx.exception), "__init__() missing 1 " +
                         "required positional argument: 'height'")

        r4 = Rectangle(1, 1)
        self.assertEqual(r4.x, 0)
        self.assertEqual(r4.y, 0)
        r4 = Rectangle(1, 2, 3)
        self.assertEqual(r4.x, 3)
        self.assertEqual(r4.y, 0)

    def test_3(self):
        ''' task 3 tests '''
        # int args checks
        with self.assertRaises(TypeError) as ctx:
            Rectangle(1.0, 2, 3, 4, 5)
        self.assertEqual(str(ctx.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as ctx:
            Rectangle(1, 2.1, 3, 4, 5)
        self.assertEqual(str(ctx.exception), 'height must be an integer')
        with self.assertRaises(TypeError) as ctx:
            Rectangle(1, 2, '3', 4, 5)
        self.assertEqual(str(ctx.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as ctx:
            Rectangle(1, 2, 3, 4 + 0j, 5)
        self.assertEqual(str(ctx.exception), 'y must be an integer')

        # int args checks precedence
        with self.assertRaises(TypeError) as ctx:
            Rectangle(1.0, '2', 3.3, 3+0j, 5)
        self.assertEqual(str(ctx.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as ctx:
            Rectangle(1, '2', 3.3, 3+0j, 5)
        self.assertEqual(str(ctx.exception), 'height must be an integer')
        with self.assertRaises(TypeError) as ctx:
            Rectangle(1, 2, 3.3, 3+0j, 5)
        self.assertEqual(str(ctx.exception), 'x must be an integer')

        # width an height limit
        with self.assertRaises(ValueError) as ctx:
            Rectangle(-1, 2, 3, 4, 5)
        self.assertEqual(str(ctx.exception), 'width must be > 0')
        with self.assertRaises(ValueError) as ctx:
            Rectangle(0, 2, 3, 4, 5)
        self.assertEqual(str(ctx.exception), 'width must be > 0')
        with self.assertRaises(ValueError) as ctx:
            Rectangle(1, -1, 3, 4, 5)
        self.assertEqual(str(ctx.exception), 'height must be > 0')
        with self.assertRaises(ValueError) as ctx:
            Rectangle(1, 0, 3, 4, 5)
        self.assertEqual(str(ctx.exception), 'height must be > 0')
        # width and height limit precedence
        with self.assertRaises(ValueError) as ctx:
            Rectangle(0, 0, 3, 4, 5)
        self.assertEqual(str(ctx.exception), 'width must be > 0')

        # x and y limit
        with self.assertRaises(ValueError) as ctx:
            Rectangle(1, 2, -3, 4, 5)
        self.assertEqual(str(ctx.exception), 'x must be >= 0')
        with self.assertRaises(ValueError) as ctx:
            Rectangle(1, 2, 3, -4, 5)
        self.assertEqual(str(ctx.exception), 'y must be >= 0')

        # x and y limit precedence
        with self.assertRaises(ValueError) as ctx:
            Rectangle(1, 2, -3, -4, 5)
        self.assertEqual(str(ctx.exception), 'x must be >= 0')

        Rectangle(1, 2, 0, 4, 5)
        Rectangle(1, 2, 1, 0, 5)
        Rectangle(1, 2, 0, 0, 5)

        # width and height vs x and y limit precedence
        with self.assertRaises(ValueError) as ctx:
            Rectangle(0, 0, -1, -1, 5)
        self.assertEqual(str(ctx.exception), 'width must be > 0')

    def test_4(self):
        ''' task 4 tests '''
        # area checks
        self.assertEqual(Rectangle(1, 2, 3, 4, 5).area(), 2)
        self.assertEqual(Rectangle(100, 200, 3, 0, 0).area(), 20000)

    def test_5(self):
        ''' task 5 tests '''
        with io.StringIO() as stout:
            with contextlib.redirect_stdout(stout):
                Rectangle(1, 1).display()
            self.assertEqual(stout.getvalue(), '#\n')

        with io.StringIO() as stout:
            with contextlib.redirect_stdout(stout):
                Rectangle(2, 3).display()
            self.assertEqual(stout.getvalue(), '##\n##\n##\n')

    def test_6(self):
        ''' task 6 tests '''
        r1 = Rectangle(1, 1)
        self.assertEqual(str(r1), '[Rectangle] ({}) 0/0 - 1/1'.format(r1.id))

        r1 = Rectangle(10, 15, 2, 3, 4)
        self.assertEqual(str(r1), '[Rectangle] (4) 2/3 - 10/15')

    def test_7(self):
        ''' task 7 tests '''
        with io.StringIO() as stout:
            with contextlib.redirect_stdout(stout):
                Rectangle(1, 1, 0, 0).display()
            self.assertEqual(stout.getvalue(), '#\n')

        with io.StringIO() as stout:
            with contextlib.redirect_stdout(stout):
                Rectangle(2, 3, 1, 1).display()
            self.assertEqual(stout.getvalue(), '\n ##\n ##\n ##\n')

        with io.StringIO() as stout:
            with contextlib.redirect_stdout(stout):
                Rectangle(2, 3, 6, 4).display()
            self.assertEqual(stout.getvalue(),
                             '\n\n\n\n      ##\n      ##\n      ##\n')

    def test_8(self):
        ''' task 8 tests '''
        r1 = Rectangle(1, 2, 3, 4, 5)
        r1.update(10)
        self.assertEqual(r1.id, 10)
        r1.update(1)
        self.assertEqual(r1.id, 1)
        r1.update()
        self.assertEqual(r1.id, 1)

        r1.update(1, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 2)

        r1.update(3, 4, 5)
        self.assertEqual(r1.id, 3)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 5)

        r1.update(5, 6, 7, 8)
        self.assertEqual(r1.id, 5)
        self.assertEqual(r1.width, 6)
        self.assertEqual(r1.height, 7)
        self.assertEqual(r1.x, 8)

        r1.update(9, 10, 11, 12, 13)
        self.assertEqual(r1.id, 9)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 11)
        self.assertEqual(r1.x, 12)
        self.assertEqual(r1.y, 13)

        r1.update(9, 10, 11, 12, 13, 15)
        self.assertEqual(r1.id, 9)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 11)
        self.assertEqual(r1.x, 12)
        self.assertEqual(r1.y, 13)

        with self.assertRaises(TypeError) as ctx:
            r1.update(1, 2.0)
        self.assertEqual(str(ctx.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as ctx:
            r1.update(1, 2, '3')
        self.assertEqual(str(ctx.exception), 'height must be an integer')

        with self.assertRaises(TypeError) as ctx:
            r1.update(1, 2, 4, 'x')
        self.assertEqual(str(ctx.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as ctx:
            r1.update(1, 2, 3, 4, 5 + 0j)
        self.assertEqual(str(ctx.exception), 'y must be an integer')

        with self.assertRaises(ValueError) as ctx:
            r1.update(1, 0)
        self.assertEqual(str(ctx.exception), 'width must be > 0')
        with self.assertRaises(ValueError) as ctx:
            r1.update(1, 2, -1)
        self.assertEqual(str(ctx.exception), 'height must be > 0')

        with self.assertRaises(ValueError) as ctx:
            r1.update(1, 2, 4, -1)
        self.assertEqual(str(ctx.exception), 'x must be >= 0')
        with self.assertRaises(ValueError) as ctx:
            r1.update(1, 2, 3, 4, -5)
        self.assertEqual(str(ctx.exception), 'y must be >= 0')

        with self.assertRaises(TypeError) as ctx:
            r1.update(1, 2, 3+0j, 'x', 'y')
        self.assertEqual(str(ctx.exception), 'height must be an integer')

    def test_9(self):
        ''' task 9 tests '''
        r1 = Rectangle(1, 2, 3, 4, 5)
        r1.update(**{'id': 10})
        self.assertEqual(r1.id, 10)
        r1.update(**{'id': 1})
        self.assertEqual(r1.id, 1)
        r1.update()
        self.assertEqual(r1.id, 1)

        r1.update(**{'id': 1, 'width': 2})
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 2)

        r1.update(**{'id': 3, 'width': 4, 'height': 5})
        self.assertEqual(r1.id, 3)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 5)

        r1.update(**{'id': 5, 'width': 6, 'height': 7, 'x': 8})
        self.assertEqual(r1.id, 5)
        self.assertEqual(r1.width, 6)
        self.assertEqual(r1.height, 7)
        self.assertEqual(r1.x, 8)

        r1.update(**{'id': 9, 'height': 11, 'width': 10, 'x': 12, 'y': 13})
        self.assertEqual(r1.id, 9)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 11)
        self.assertEqual(r1.x, 12)
        self.assertEqual(r1.y, 13)

        r1.update(**{'id': 9, 'width': 10, 'height': 11,
                     'x': 12, 'y': 13, 'z': 15})
        self.assertEqual(r1.id, 9)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 11)
        self.assertEqual(r1.x, 12)
        self.assertEqual(r1.y, 13)

        # check that kwargs are ignored if any arg is present
        r1.update(1, 2, **{'width': 3, 'height': 4})
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 11)

        with self.assertRaises(TypeError) as ctx:
            r1.update(**{'id': 1, 'width': 2.0})
        self.assertEqual(str(ctx.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as ctx:
            r1.update(**{'id': 1, 'width': 2, 'height': '3'})
        self.assertEqual(str(ctx.exception), 'height must be an integer')

        with self.assertRaises(TypeError) as ctx:
            r1.update(**{'id': 1, 'width': 2, 'height': 4, 'x': 'x'})
        self.assertEqual(str(ctx.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as ctx:
            r1.update(**{'id': 1, 'width': 2, 'height': 3,
                         'x': 4, 'y': 5 + 0j})
        self.assertEqual(str(ctx.exception), 'y must be an integer')

        with self.assertRaises(ValueError) as ctx:
            r1.update(**{'id': 1, 'width': 0})
        self.assertEqual(str(ctx.exception), 'width must be > 0')
        with self.assertRaises(ValueError) as ctx:
            r1.update(**{'id': 1, 'width': 2, 'height': -1})
        self.assertEqual(str(ctx.exception), 'height must be > 0')

        with self.assertRaises(ValueError) as ctx:
            r1.update(**{'id': 1, 'width': 2, 'height': 4, 'x': -1})
        self.assertEqual(str(ctx.exception), 'x must be >= 0')
        with self.assertRaises(ValueError) as ctx:
            r1.update(**{'id': 1, 'width': 2, 'height': 3, 'x': 4, 'y': -5})
        self.assertEqual(str(ctx.exception), 'y must be >= 0')

        with self.assertRaises(TypeError) as ctx:
            r1.update(**{'id': 1, 'width': 2, 'height': 3+0j,
                         'x': 'x', 'y': 'y'})
        self.assertEqual(str(ctx.exception), 'height must be an integer')

    def test_13(self):
        ''' task 13 tests '''

        r1 = Rectangle(1, 2, 3, 4, 5)
        d1 = {'width': 1, 'height': 2, 'x': 3, 'y': 4, 'id': 5}
        self.assertEqual(r1.to_dictionary(), d1)
        r1.id = 8
        d1['id'] = 8
        self.assertEqual(r1.to_dictionary(), d1)

        r1.update(1, 2)
        d1['id'] = 1
        d1['width'] = 2
        self.assertEqual(r1.to_dictionary(), d1)

        r1.update(**{'x': 8, 'y': 1, 'height': 4})
        d1['x'] = 8
        d1['y'] = 1
        d1['height'] = 4
        self.assertEqual(r1.to_dictionary(), d1)

        dr = r1.to_dictionary()
        r1.width = 10
        self.assertTrue(r1.to_dictionary() != dr)
        dr['height'] = 20
        self.assertTrue(r1.height != 20)
