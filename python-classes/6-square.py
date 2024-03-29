#!/usr/bin/python3
"""Write a class Square that defines a square by:
property def size(self): to retrieve it
property setter def size(self, value): to set it:
Instantiation with optional size: def __init__(self, size=0):
size must be an integer, otherwise raise a TypeError
exception with the message size must be an integer
if size is less than 0, raise a ValueError exception
with the message size must be >= 0
Public instance method: def area(self): that returns the current square area
Print a square
"""


class Square:
    """It takes size arg
    Args:
    size: Size of square
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(item, int) and item >= 0 for item in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for y_coordinates in range(self.__position[1]):
                print()
            for height in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size, end="")
                print()
