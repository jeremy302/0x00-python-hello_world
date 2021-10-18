#!/usr/bin/python3
''' module for the Class: Base '''
import os
import json
import csv


class Base:
    ''' Base class for all shapes '''
    __nb_objects = 0

    def __init__(self, id=None):
        ''' Initializes a new instance with an id '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' converts a dict to a json string '''
        if list_dictionaries in [None, []]:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        ''' saves a Base instance to a file '''
        if list_objs is None:
            list_objs = []
        with open('{}.json'.format(cls.__name__), 'w') as file:
            file.write(cls.to_json_string(
                [{'id': obj.id} if type(obj) is Base else obj.to_dictionary()
                 for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        ''' converts a json string to a list of objects '''
        if json_string in [None, '']:
            return []
        return json.loads(json_string)
