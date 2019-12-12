#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv) - 1
    if length == 0:
        print("{:d} arguments.".format(length))
    elif length == 1:
        print("{:d} argument:".format(length))
    else:
        print("{:d} arguments:".format(length))
    for i, arg in enumerate(sys.argv):
        if i > 0:
            print("{:d}: {}".format(i + 1, arg))
