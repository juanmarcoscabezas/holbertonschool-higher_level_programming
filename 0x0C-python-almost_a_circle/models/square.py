#!/usr/bin/python3


"""
Square class
"""

from models.rectangle import Rectangle


class Square(Rectangle):

    """Square class definition"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overrifing str method"""
        text = "[Square] ({:d}) {:d}/{:d} - {:d}"
        return text.format(self.id, self.x, self.y, self.width, self.height)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value
