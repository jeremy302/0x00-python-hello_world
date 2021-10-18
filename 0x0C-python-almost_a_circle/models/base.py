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

    @classmethod
    def create(cls, **dictionary):
        ''' creates a Base object from a dictionary '''
        arg_ls = ([] if cls is Base else [1, 1]
                  if cls.__name__ == 'Rectangle' else [1]
                  if cls.__name__ == 'Square' else
                  list(1 for i in
                       range(cls.__init__.__code__.co_argcount - 2)))
        obj = cls(*(arg_ls))
        # obj.__dict__.update(dictionary)
        for k, v in dictionary.items():
            setattr(obj, k, v)
        return obj

    @classmethod
    def load_from_file(cls):
        ''' loads Base objects from a file '''
        filenm = '{}.json'.format(cls.__name__)
        if not os.path.isfile(filenm):
            return []
        with open(filenm, 'r') as file:
            ls = cls.from_json_string(file.read())
            return [cls.create(**obj) for obj in ls]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        ''' saves a list of Base objects to a file '''
        with open('{}.csv'.format(cls.__name__), 'w') as file:
            writer = csv.writer(file, delimiter=',')
            for obj in list_objs:
                if getattr(obj, 'size', None) is not None:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])
                else:
                    writer.writerow(
                        [obj.id, obj.width, obj.height, obj.x, obj.y])
