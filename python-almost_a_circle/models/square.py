#!/usr/bin/python3
"""And now, the Square!"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """A new class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Update the class"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - \
{self.width}")

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args:
            names = ["id", "size", "x", "y"]
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
