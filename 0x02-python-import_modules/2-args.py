#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("{:d} argument:".format(len(sys.argv)))
    else:
        print("{:d} arguments:".format(len(sys.argv)))
    for i, arg in enumerate(sys.argv):
        print("{:d}: {}".format(i + 1, arg))
