#!/usr/bin/python3
for i in range(122, 96, -1):
    turn_uppercase = 0
    if (i % 2 != 0):
        turn_uppercase = 32
    print("{}".format(chr(i - turn_uppercase)), end='')
