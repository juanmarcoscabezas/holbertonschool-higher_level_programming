#!/usr/bin/python3


"""
Module print_square
Prints a squeare with the character #

"""


def print_square(size):

    """This function prints a square with the character #

       >>> print_square(2)
       ##
       ##
    """
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
