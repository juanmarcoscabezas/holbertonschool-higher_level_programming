#!/usr/bin/python3


def read_lines(filename="", nb_lines=0):
    n_lines = 0
    with open(filename, 'r') as f:
        for line in f:
            n_lines += 1

    with open(filename, 'r') as f:
        if n_lines < nb_lines or nb_lines <= 0:
            print(f.read(), end="")
            return
        for n, line in enumerate(f):
            if n < nb_lines:
                print(line, end="")
