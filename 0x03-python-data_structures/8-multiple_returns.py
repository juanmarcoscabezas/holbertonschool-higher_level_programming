#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) > 0:
        res = len(sentence), sentence[0]
        return res
    res = len(sentence), None
    return res
