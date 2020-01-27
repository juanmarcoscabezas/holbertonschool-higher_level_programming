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

    def update(self, *args, **kwargs):
        """update object"""
        size = 0
        for i, arg in enumerate(args):
            if i == 0:
                self.id = arg
            if i == 1:
                self.width = arg
                self.height = arg
            if i == 2:
                self.x = arg
            if i == 3:
                self.y = arg
            size += 1
        if size == 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.width = value
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """parse to dictionary"""
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
