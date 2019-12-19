#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_new = set()
    for val in set_1:
        if not (val in set_2):
            set_new.add(val)
    for val in set_2:
        if not (val in set_1):
            set_new.add(val)
    return set_new
