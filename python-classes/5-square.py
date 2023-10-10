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

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        assert isinstance(value, int), "size must be an integer"
        assert value >= 0, "size must be >= 0"
        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
