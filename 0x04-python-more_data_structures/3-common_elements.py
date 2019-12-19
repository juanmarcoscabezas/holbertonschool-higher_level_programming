#!/usr/bin/python3
def common_elements(set_1, set_2):
    set_new = set()
    for val in set_1:
        if val in set_2:
            set_new.add(val)
    return set_new
