#!/usr/bin/python3


"""
Rectangle class
"""

from models.base import Base


class Rectangle(Base):

    """Rectangle class definition"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """overrifing str method"""
        text = "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
        return text.format(self.id, self.x, self.y, self.width, self.height)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """rectangle area"""
        return self.width * self.height

    def display(self):
        """prints the rectangle with #"""
        for y in range(self.y):
            print()
        for h in range(self.height):
            for x in range(self.x):
                    print(" ", end="")
            for w in range(self.width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """update object"""
        size = 0
        for i, arg in enumerate(args):
            if i == 0:
                self.id = arg
            if i == 1:
                self.width = arg
            if i == 2:
                self.height = arg
            if i == 3:
                self.x = arg
            if i == 4:
                self.y = arg
            size += 1
        if size == 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
