#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        res = fct(*args)
    except BaseException as be:
        sys.stderr.write("Exception: %s\n" % be)
        res = None
    finally:
        return res
