#!/usr/bin/python3
def square_m(number):
        return (number ** 2)

def square_matrix_simple(matrix=[]):
    new_matrix = [list(map(square_m, vector )) for vector in matrix]
    return (new_matrix)
