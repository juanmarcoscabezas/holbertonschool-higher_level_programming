#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) == 0 or not my_list:
        return None
    new_list = list(my_list)
    for i, item in enumerate(new_list):
        if item % 2 == 0:
            new_list[i] = True
        else:
            new_list[i] = False
    return new_list
