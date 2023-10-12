#!/usr/bin/python3
"""An empty class Rectangle that defines a rectangle"""


class Rectangle:
    """Empty class"""

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        assert isinstance(value, int), "width must be an integer"
        assert value >= 0, "width must be >= 0"
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        assert isinstance(value, int), "height must be an integer"
        assert value >= 0, "height must be >= 0"
        self.__height = value
