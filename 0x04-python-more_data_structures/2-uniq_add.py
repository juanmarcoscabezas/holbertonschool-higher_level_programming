#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    total = 0
    for element in my_list:
        if not (element in new_list):
            new_list.append(element)
            total += element
    return total
