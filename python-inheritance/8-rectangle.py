#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""class BaseGeometry.
Public instance method: def area(self):
"""


class Rectangle(BaseGeometry):
    """class"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
