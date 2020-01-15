#!/usr/bin/python3


class Rectangle:

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        result = ""
        if self.__width == 0 or self.__height == 0:
            return result
        for h in range(self.__height):
            for w in range(self.__width):
                result += str(self.print_symbol)
            if h < self.__height - 1:
                result += "\n"
        return result

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def __repr__(self):
        result = "Rectangle("
        result += str(self.__width) + ", "
        result += str(self.__height) + ")"
        return result

    @property
    def width(self):

        return self.__width

    @width.setter
    def width(self, width):

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):

        return self.__height

    @height.setter
    def height(self, height):

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):

        return self.__width * self.__height

    def perimeter(self):

        if self.__width == 0 or self.height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def bigger_or_equal(rect_1, rect_2):

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
