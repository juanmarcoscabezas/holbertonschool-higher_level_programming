#!/usr/bin/python3


"""
Module add-integer
adds two integers

"""


def add_integer(a, b=98):

    """ This function returns the add of two ints
        Throws and error if the values are not int or float
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
