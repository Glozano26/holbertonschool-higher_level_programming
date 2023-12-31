#!/usr/bin/python3
"""Same class or inherit from"""


def inherits_from(obj, a_class):
    """function that returns True if the object is an instance
    of, or if the object is an instance of a class that inherited from,
     the specified class ; otherwise False.
     """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
