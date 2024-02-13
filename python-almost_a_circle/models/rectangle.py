#!/usr/bin/python3
'''Write the first class Base'''
from .base import Base


class Rectangle(Base):
    '''class Base'''
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        '''Return area'''
        return self.__height * self.__width

    def display(self):
        '''Dispaly rectangle'''
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        '''Overwrite str'''
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y}"
                f" - {self.width}/{self.height}")

    def update(self, *args, **kwargs):
        '''Update class that assigns an argument'''
        arg_list = ["id", "width", "height", "x", "y"]
        for arg_name, arg_value in zip(arg_list, args):
            setattr(self, arg_name, arg_value)
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        '''dictionary'''
        return {'id': {self.id}, 'width': {self.width},
                'height': {self.height}, 'x': {self.x}, 'y': {self.y}}
