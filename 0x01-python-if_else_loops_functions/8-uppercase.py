#!/usr/bin/python3
def uppercase(str):
    for s in str:
        acum = 0
        if (ord(s) >= 97 and ord(s) <= 122):
            acum = 32
        print("{}".format(chr(ord(s) - acum)), end='')
    else:
        print()
