#!/usr/bin/python3
"""This script displays the value of the id variable """

if __name__ == "__main__":
    import urllib.request
    from sys import argv
    with urllib.request.urlopen(argv[1]) as response:
        header = response.info()
        for key, val in header.items():
            if key == 'X-Request-Id':
                print(val)
