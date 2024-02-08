#!/usr/bin/python3
"""Write a class Square that inherits
    from Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class"""
    def __init__(self, size):
        self.__size = size

    def area(self):
        return self.__size**2
