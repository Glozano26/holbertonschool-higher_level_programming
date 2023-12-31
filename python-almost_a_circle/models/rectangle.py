#!/usr/bin/python3
"""first class Base"""

from models.base import Base


class Rectangle(Base):
    """This class will be the “base” of all other classes in this project.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Area first"""
        return (self.__width * self.__height)

    def display(self):
        """Display #"""
        print(self.y * "\n", end="")
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Update the class"""
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args:
            names = ["id", "width", "height", "x", "y"]
            for value, name in zip(args, names):
                setattr(self, name, value)
        for name, value in kwargs.items():
            if hasattr(self, name):
                setattr(self, name, value)

    def to_dictionary(self):
        """Rectangle instance to dictionary representation"""
        claves = ["id", "width", "height", "x", "y"]
        value = [self.id, self.width, self.height, self.x, self.y]
        my_dict = dict(zip(claves, value))
        return my_dict
