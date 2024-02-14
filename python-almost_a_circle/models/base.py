#!/usr/bin/python3
'''Write the first class Base'''
import json


class Base:
    '''class Base'''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        '''return a json string of a list list dictionaries'''
        if list_dictionaries is not None:
            return json.dumps(list_dictionaries)
        return []
