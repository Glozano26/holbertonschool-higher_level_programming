#!/usr/bin/python3
"""an empty class Square that defines a square"""


class Square:
    """Square class"""

    def __init__(self, size=0):
        assert isinstance(size, int), "size must be an integer"
        assert size >= 0, "size must be >= 0"
        self.__size = size
    def area(self):
        return self.__size * self.__size
