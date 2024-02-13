#!/usr/bin/python3
'''Write the first class Base'''
from .rectangle import Rectangle


class Square(Rectangle):
    '''class Rectangle'''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id, size, size, x, y)

    def __str__(self):
        '''Overwrite str square'''
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")
