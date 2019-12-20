#!/usr/bin/python3
def roman_to_int(roman_string):
    number = 0
    if type(roman_string) == str:
        for i, letter in enumerate(roman_string):
            val = roman_numbers(letter)
            if i < len(roman_string) - 1:
                if roman_numbers(roman_string[i + 1]) > val:
                    number -= val
                else:
                    number += val
            else:
                number += val
    return number


def roman_numbers(letter):
    number = 0
    if letter == "I":
        number += 1
    if letter == "V":
        number += 5
    if letter == "X":
        number += 10
    if letter == "L":
        number += 50
    if letter == "C":
        number += 100
    if letter == "D":
        number += 500
    if letter == "M":
        number += 1000
    return number
