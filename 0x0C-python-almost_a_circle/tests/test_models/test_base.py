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
