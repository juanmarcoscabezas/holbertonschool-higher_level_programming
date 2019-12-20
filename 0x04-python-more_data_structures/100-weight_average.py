#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) > 0:
        multi = 0
        sum_div = 0
        for tup in my_list:
            multi += tup[0] * tup[1]
            sum_div += tup[1]
        return multi / sum_div
    return 0
