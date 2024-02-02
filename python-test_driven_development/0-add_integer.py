#!/usr/bin/python3
"""
Adds two numbers together.
"""


def add_integer(a, b=98):
    """
    Parameters:
    a (int): The first number.
    b (int): The second number.
    Returns:
    int: The sum of x and y.
    Example:
    add(2, 3)
    5
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a + b)
