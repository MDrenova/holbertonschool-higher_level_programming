#!/usr/bin/python3
'''

Module to print a given text
and insterting newlines when encountaring
this type of characters . ? !
'''


def print_square(size):
    '''

    Function that prints the text given as argument
    and inserting newlines when encountaring this
    type of characters . ? !
    '''
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        print("#" * size, end="")
        print()
