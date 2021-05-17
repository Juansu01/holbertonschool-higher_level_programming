#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    
    try:
        print("{:d}".format(value))
        return True
    except TypeError as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return False
    except ValueError as erro:
        print("Exception: {}".format(erro), file=sys.stderr)
        return False
