#!/usr/bin/python3
"""an empty class Square that defines a square"""


class Square:
    """Square class"""

    def __init__(self, size=0, position=(0, 0)):
        assert isinstance(size, int), "size must be an integer"
        assert size >= 0, "size must be >= 0"
        self.size = size
        self.position = position

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
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print(" " * self.__position[0], end=" ")
                print("#" * self.size)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if self.__size == 0:
            print()
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value[0], value[1]
