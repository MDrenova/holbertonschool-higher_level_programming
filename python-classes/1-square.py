#!/usr/bin/python3
"""Write a class Square that defines a square by: 
Private instance attribute: size
Instantiation with size (no type/value verification)
You are not allowed to import any module
"""


class Square:
    """It takes size arg
    Args:
    size: Size of square
    """
    def __init__(self, size):
        self.__size = size
