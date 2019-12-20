#!/usr/bin/python3
def best_score(a_dictionary):
    best = ""
    score = 0
    has_change = False
    if a_dictionary:
        for key in a_dictionary:
            if a_dictionary[key] > score:
                score = a_dictionary[key]
                best = key
            has_change = True
    if best != "":
        return best
    return None
