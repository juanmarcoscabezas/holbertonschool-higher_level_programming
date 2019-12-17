#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    values = [0, 0, 0, 0]
    if len(tuple_a) > 0:
        values[0] = tuple_a[0]
    if len(tuple_a) > 1:
        values[1] = tuple_a[1]

    if len(tuple_b) > 0:
        values[2] = tuple_b[0]
    if len(tuple_b) > 1:
        values[3] = tuple_b[1]

    res = values[0] + values[2], values[1] + values[3]
    return res
