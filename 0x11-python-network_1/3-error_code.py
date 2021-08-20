#!/usr/bin/python3
""" This module handles errors """

if __name__ == "__main__":
    import urllib.request
    from sys import argv

    try:
        with urllib.request.urlopen(argv[1]) as response:
            resp = response.read()
            print(resp.decode('utf-8'))
    except urllib.error.HTTPError as my_err:
        print('Error code: {}'.format(my_err.code))
