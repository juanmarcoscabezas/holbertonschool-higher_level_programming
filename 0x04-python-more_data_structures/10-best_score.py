#!/usr/bin/python3
def best_score(a_dictionary):
    score = 0
    has_change = False
    if a_dictionary:
        for val in a_dictionary.values():
            if val > 0:
                score = val
            has_change = True
    if has_change:
        return score
    return None
