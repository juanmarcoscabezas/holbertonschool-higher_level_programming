#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for vector in matrix:
        for i, element in enumerate(vector):
            if i != 0:
                print(" ", end="")
            print("{:d}".format(element), end="")
        print()
