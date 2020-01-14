#!/usr/bin/python3


"""
Module matrix_divided
Divides all elements of a matrix

"""


def matrix_divided(matrix, div):

    """This function divides all elements of a matrix

       >>> matrix_divided([1, 2, 3], [4, 5, 6])
    """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    if any(type(vector) is not list for vector in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    if len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    size = len(matrix[0])
    for vector in matrix:
        if len(vector) != size:
            raise TypeError("Each row of the matrix must have the same \
size")
        if len(vector) == 0:
            raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
        for value in vector:
            if type(value) is not int and type(value) is not float:
                raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError('division by zero')
    return(
        list(map(lambda v: list(map(lambda n: round(n / div, 2), v)), matrix))
    )
