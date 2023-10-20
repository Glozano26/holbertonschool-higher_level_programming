#!/usr/bin/python3
"""Full rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Definition of the class Rectangle using the Rectangle"""
    def __init__(self, size):

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """return area of square"""
        return self.__size * self.__size

    def __str__(self):
        """Return representation of square#2"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
