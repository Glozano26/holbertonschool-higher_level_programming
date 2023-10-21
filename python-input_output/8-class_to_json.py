#!/usr/bin/python3
"""function that returns the dictionary description with simple data structure
"""


def class_to_json(obj):
    """function that returns the dictionary description with
        simple data structure
        Args:
            obj : object
        Return:
            Object
        """
    return obj.__dict__
