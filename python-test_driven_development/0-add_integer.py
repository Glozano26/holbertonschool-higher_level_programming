#!/usr/bin/python3
"""Integers addition
Adds two integers (a, b) and returns integer sum
a and b int or float
Floats get converted to integers, all others raise TypeError
"""


def add_integer(a, b=98):
    """adds two integers
    Returns: integer sum
    """
    if not isinstance(a, float) and not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, float) and not isinstance(b, int):
        raise TypeError("b must be an integer")

    return int(a + b)
