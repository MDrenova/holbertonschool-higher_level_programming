#!/usr/bin/python3
"""
Print square
"""
def print_square(size):
    '''

    Function that prints the
    area of the square
    '''
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size == 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) or size < 0:
        raise TypeError("size must be an integer")
    for row in range(size):
        print("#" * size, end="")
        print()
