#!/usr/bin/python3


def number_of_lines(filename=""):
    with open(filename, 'r') as f:
        n_lines = 0
        for line in f:
            n_lines += 1
        return n_lines
