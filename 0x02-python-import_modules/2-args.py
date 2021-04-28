#!/usr/bin/python3

import sys

if __name__ == '__main__':
    arguments = len(sys.argv)
    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(arguments - 1))
        for i in range(1, arguments):
            print("{}: {}".format(i, sys.argv[i]))
