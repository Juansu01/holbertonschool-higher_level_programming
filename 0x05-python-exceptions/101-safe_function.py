#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except ZeroDivisionError as diverr:
        print("Exception: {}".format(diverr), file=sys.stderr)
        return None
    except IndexError as inerr:
        print("Exception: {}".format(inerr), file=sys.stderr)
        return None
