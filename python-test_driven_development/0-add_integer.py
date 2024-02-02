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
    if not all(isinstance(i, (int, float)) for i in (a, b)):
        raise TypeError("a must be an integer or b must be an integer")
    else:
        return int(a + b)
