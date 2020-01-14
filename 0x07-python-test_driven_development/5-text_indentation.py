#!/usr/bin/python3


"""
Module text_indentation
Prints a text with 2 new lines after each . ? :

"""


def text_indentation(text):

    """This function prints a text

       >>> add_integer(10, 20)
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    jump = True
    for i in range(len(text)):
        if jump is True and text[i] == " ":
            continue
        if text[i] in ".?:":
            print("{}\n".format(text[i]))
            jump = True
        else:
            print("{}".format(text[i]), end="")
            jump = False
