#!/usr/bin/python3
"""Full rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Definition of the class Rectangle using the BaseGometry"""
    def __init__(self, width, height):

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """return the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return representation of a Rectangle."""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
