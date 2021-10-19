#!/usr/bin/python3
''' testing module '''
from unittest import TestCase
import json
import os
import csv

Base = __import__('models.base').base.Base
Rectangle = __import__('models.rectangle').rectangle.Rectangle
Square = __import__('models.square').square.Square


class TestBase(TestCase):
    ''' Base tests class '''

    @staticmethod
    def base_json(obj):
        ''' gets the dict representation of a Base shape '''
        return {'id': obj.id}

    @staticmethod
    def rect_json(obj):
        ''' gets the dict representation of a Rectangle shape '''
        return {"id": obj.id, "width": obj.width, "height": obj.height,
                "x": obj.x, "y": obj.y}

    @staticmethod
    def sq_json(obj):
        ''' gets the dict representation of a Square shape '''
        return {"id": obj.id, "size": obj.size, "x": obj.x, "y": obj.y}

    def test_0(self):
        ''' tests that nb_objects is private '''
        self.assertFalse('nb_objects' in dir(Base))
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base().id, 3)
        self.assertEqual(Base(0).id, 0)
        self.assertEqual(Base().id, 4)
        self.assertEqual(Base(-10).id, -10)
        self.assertEqual(Base(10).id, 10)
        self.assertEqual(Base().id, 5)

    def test_15(self):
        ''' task 15 tests '''
        self.assertEqual(Base.to_json_string(None), '[]')
        self.assertEqual(Base.to_json_string([]), '[]')
        self.assertEqual(Base.to_json_string([{}]), '[{}]')
        self.assertEqual(Base.to_json_string([{'key': 'val'}]),
                         '[{"key": "val"}]')

    def test_16(self):
        ''' task 16 tests '''
        Base.save_to_file(None)
        with open('Base.json', 'r') as file:
            self.assertEqual(file.read(), Base.to_json_string(None))
        Base.save_to_file([])
        with open('Base.json', 'r') as file:
            self.assertEqual(file.read(), Base.to_json_string([]))

        b1 = Base(1)
        b2 = Base(2)
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(5, 4, 3, 2, 1)
        s1 = Square(1, 2, 3, 4)
        s2 = Square(4, 3, 2, 1)

        Base.save_to_file(None)
        with open('Base.json', 'r') as file:
            self.assertEqual(json.loads(file.read()), [])
        Base.save_to_file([])
        with open('Base.json', 'r') as file:
            self.assertEqual(json.loads(file.read()), [])
        Base.save_to_file([b1])
        with open('Base.json', 'r') as file:
            self.assertEqual(json.loads(file.read()), [TestBase.base_json(b1)])
        Base.save_to_file([b1, b2])
        with open('Base.json', 'r') as file:
            self.assertEqual(json.loads(file.read()),
                             [TestBase.base_json(b1), TestBase.base_json(b2)])
        Base.save_to_file([b1, b2, b2])
        with open('Base.json', 'r') as file:
            self.assertEqual(json.loads(file.read()),
                             [TestBase.base_json(b1), TestBase.base_json(b2),
                              TestBase.base_json(b2)])

        Rectangle.save_to_file(None)
        with open('Rectangle.json', 'r') as file:
            self.assertEqual(json.loads(file.read()), [])
        os.unlink('Rectangle.json')
        Rectangle.save_to_file([])
        with open('Rectangle.json', 'r') as file:
            self.assertEqual(json.loads(file.read()), [])
        Rectangle.save_to_file([r1])
        with open('Rectangle.json', 'r') as file:
            self.assertEqual(json.loads(file.read()), [TestBase.rect_json(r1)])
        Rectangle.save_to_file([r1, r2])
        with open('Rectangle.json', 'r') as file:
            self.assertEqual(json.loads(file.read()),
                             [TestBase.rect_json(r1), TestBase.rect_json(r2)])
        Rectangle.save_to_file([r1, r2, r2])
        with open('Rectangle.json', 'r') as file:
            self.assertEqual(json.loads(file.read()),
                             [TestBase.rect_json(r1),
                              TestBase.rect_json(r2), TestBase. rect_json(r2)])

        Square.save_to_file(None)
        with open('Square.json', 'r') as file:
            self.assertEqual(json.loads(file.read()), [])
        os.unlink('Square.json')
        Square.save_to_file([])
        with open('Square.json', 'r') as file:
            self.assertEqual(json.loads(file.read()), [])
        Square.save_to_file([s1])
        with open('Square.json', 'r') as file:
            self.assertEqual(json.loads(file.read()), [TestBase.sq_json(s1)])
        Square.save_to_file([s1, s2])
        with open('Square.json', 'r') as file:
            self.assertEqual(json.loads(file.read()),
                             [TestBase.sq_json(s1), TestBase.sq_json(s2)])
        Square.save_to_file([s1, s2, s2])
        with open('Square.json', 'r') as file:
            self.assertEqual(json.loads(file.read()),
                             [TestBase.sq_json(s1),
                              TestBase.sq_json(s2), TestBase.sq_json(s2)])

    def test_17(self):
        ''' task 17 tests '''
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(''), [])
        self.assertEqual(Base.from_json_string('[]'), [])
        self.assertEqual(Base.from_json_string('[{}]'), [{}])
        self.assertEqual(Base.from_json_string('[{"key": "val"}]'),
                         [{'key': 'val'}])

    def test_18(self):
        ''' task 18 tests '''
        # n = Base().id
        self.assertEqual(Base.create(id=3).id, 3)
        # self.assertEqual(Base.create().id, n + 1)
        # self.assertEqual(Base.create(a=4).id, n + 2)
        # n += 2

        r1 = Rectangle.create()
        self.assertEqual(type(r1), Rectangle)
        # self.assertEqual(r1.id, n + 1)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r1 = Rectangle.create(width=5, height=6)
        # self.assertEqual(r1.id, n + 2)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 6)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r1 = Rectangle.create(width=5, height=6, x=7, y=8, id=9)
        self.assertEqual(r1.id, 9)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 6)
        self.assertEqual(r1.x, 7)
        self.assertEqual(r1.y, 8)
        # n += 2

        s1 = Square.create()
        self.assertEqual(type(s1), Square)
        # self.assertEqual(s1.id, n + 1)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

        s1 = Square.create(size=5)
        # self.assertEqual(s1.id, n + 2)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

        s1 = Square.create(size=5, x=7, y=8, id=9)
        self.assertEqual(s1.id, 9)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.x, 7)
        self.assertEqual(s1.y, 8)

        with self.assertRaises(TypeError) as ctx:
            Rectangle.create(width=1.0)
        self.assertEqual(str(ctx.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as ctx:
            Rectangle.create(x='1')
        self.assertEqual(str(ctx.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as ctx:
            Square.create(size=1.0)
        self.assertEqual(str(ctx.exception), 'width must be an integer')

    def test_19(self):
        ''' task 19 tests '''
        os.remove('Base.json')
        os.remove('Rectangle.json')
        os.remove('Square.json')

        self.assertEqual(Base.load_from_file(), [])
        with open('Base.json', 'w') as file:
            file.write('[{"id": 5}, {"id": 6}, {"id": 7}]')
        b_ls = Base.load_from_file()
        b1 = b_ls[0]
        self.assertEqual(len(b_ls), 3)
        self.assertEqual(b1.id, 5)

        self.assertEqual(Rectangle.load_from_file(), [])
        with open('Rectangle.json', 'w') as file:
            file.write('[{"id": 5, "width": 3, "height": 4}]')
        b_ls = Rectangle.load_from_file()
        b1 = b_ls[0]
        self.assertEqual(len(b_ls), 1)
        self.assertEqual(b1.id, 5)
        self.assertEqual(b1.width, 3)
        self.assertEqual(b1.height, 4)

        with open('Rectangle.json', 'w') as file:
            file.write('[{"id": 5, "width": 3, "height": 4, "x": 0, "y": 2}]')
        b_ls = Rectangle.load_from_file()
        b1 = b_ls[0]
        self.assertEqual(len(b_ls), 1)
        self.assertEqual(b1.id, 5)
        self.assertEqual(b1.width, 3)
        self.assertEqual(b1.height, 4)
        self.assertEqual(b1.x, 0)
        self.assertEqual(b1.y, 2)

        self.assertEqual(Square.load_from_file(), [])
        self.assertEqual(Square.load_from_file(), [])
        with open('Square.json', 'w') as file:
            file.write('[{"id": 5, "size": 3}]')
        b_ls = Square.load_from_file()
        b1 = b_ls[0]
        self.assertEqual(len(b_ls), 1)
        self.assertEqual(b1.id, 5)
        self.assertEqual(b1.size, 3)

        with open('Square.json', 'w') as file:
            file.write('[{"id": 5, "size": 4, "x": 0, "y": 2}]')
        b_ls = Square.load_from_file()
        b1 = b_ls[0]
        self.assertEqual(len(b_ls), 1)
        self.assertEqual(b1.id, 5)
        self.assertEqual(b1.size, 4)
        self.assertEqual(b1.x, 0)
        self.assertEqual(b1.y, 2)

        with open('Rectangle.json', 'w') as file:
            file.write('[{"id": 5, "width": "3", "height": 4, ' +
                       '"x": 0, "y": 2}]')
        with self.assertRaises(TypeError) as ctx:
            Rectangle.load_from_file()
        self.assertEqual(str(ctx.exception), 'width must be an integer')

        with open('Rectangle.json', 'w') as file:
            file.write('[{"id": 5, "width": 3, "height": 4, ' +
                       '"x": "0", "y": 2}]')
        with self.assertRaises(TypeError) as ctx:
            Rectangle.load_from_file()
        self.assertEqual(str(ctx.exception), 'x must be an integer')

        with open('Square.json', 'w') as file:
            file.write('[{"id": 5, "size": "3", "x": 0, "y": 2}]')
        with self.assertRaises(TypeError) as ctx:
            Square.load_from_file()
        self.assertEqual(str(ctx.exception), 'width must be an integer')

    def test_20(self):
        ''' task 20 tests '''
        Rectangle.save_to_file_csv([])
        with open('Rectangle.csv', 'r') as file:
            rows = list(csv.reader(file))
            self.assertEqual(rows, [])
        r_ls = Rectangle.load_from_file_csv()
        self.assertEqual(type(r_ls), list)
        self.assertEqual(len(r_ls), 0)

        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(5, 4, 3, 2, 1)
        Rectangle.save_to_file_csv([r1, r2])
        with open('Rectangle.csv', 'r') as file:
            rows = list(csv.reader(file))
            self.assertEqual([r for r in rows if r],
                             [['5', '1', '2', '3', '4'],
                              ['1', '5', '4', '3', '2']])
        r_ls = Rectangle.load_from_file_csv()
        self.assertEqual(type(r_ls), list)
        self.assertEqual(len(r_ls), 2)
        self.assertEqual([r.to_dictionary() for r in r_ls],
                         [r1.to_dictionary(), r2.to_dictionary()])

        Square.save_to_file_csv([])
        with open('Square.csv', 'r') as file:
            rows = list(csv.reader(file))
            self.assertEqual(rows, [])
        s_ls = Square.load_from_file_csv()
        self.assertEqual(type(s_ls), list)
        self.assertEqual(len(s_ls), 0)

        s1 = Square(2, 3, 4, 5)
        s2 = Square(5, 4, 3, 2)
        Square.save_to_file_csv([s1, s2])
        with open('Square.csv', 'r') as file:
            rows = list(csv.reader(file))
            self.assertEqual([r for r in rows if r],
                             [['5', '2', '3', '4'], ['2', '5', '4', '3']])
        s_ls = Square.load_from_file_csv()
        self.assertEqual(type(s_ls), list)
        self.assertEqual(len(s_ls), 2)
        self.assertEqual([s.to_dictionary() for s in s_ls],
                         [s1.to_dictionary(), s2.to_dictionary()])
