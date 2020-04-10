#!/usr/bin/python3

"""Technical interview
"""


def find_peak(list_of_integers):
    """"Finds a peak in a list"""
    if list_of_integers:
        if len(list_of_integers) == 1:
            return list_of_integers[0]
        if list_of_integers[0] > list_of_integers[1]:
            return list_of_integers[0]
        if list_of_integers[-1] > list_of_integers[-2]:
            return list_of_integers[-1]

        mid_val = len(list_of_integers) // 2
        if list_of_integers[mid_val] >= list_of_integers[mid_val + 1] \
                and list_of_integers[mid_val] >= list_of_integers[mid_val - 1]:
            return list_of_integers[mid_val]
        if list_of_integers[mid_val - 1] > list_of_integers[mid_val]:
            return find_peak(list_of_integers[:mid_val])
        if list_of_integers[mid_val + 1] > list_of_integers[mid_val]:
            return find_peak(list_of_integers[mid_val + 1:])
