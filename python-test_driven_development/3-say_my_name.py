#!/usr/bin/python3
"""Integers addition
Adds two integers (a, b) and returns integer sum
a and b int or float
Floats get converted to integers, all others raise TypeError
"""
def say_my_name(first_name, last_name=""):
    """adds two integers
    Returns: integer sum
    """
    if isinstance(first_name, str):
        print("My name is {:s}".format(first_name), end="")
    else:
        raise TypeError("first_name must be a string")
    if isinstance(last_name, str):
        print(" {:s}".format(last_name))
    elif last_name is not None:
        raise TypeError("last_name must be a string")
    else:
        print(" ")
