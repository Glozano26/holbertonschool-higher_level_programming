#!/usr/bin/python3
"""Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Geometry module"""

class Rectangle(BaseGeometry):
    """Definition of the class Rectangle using the BaseGometry"""
    def __init__(self, width, height):
        """width and height must be private. No getter or setter
        width and height must be positive integers, validated by integer_validator
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
