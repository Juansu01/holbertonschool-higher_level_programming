#!/usr/bin/python3
"""This module shows a status """
if __name__ == "__main__":
    from sys import argv
    import requests
    ema = {'email': argv[2]}
    r = requests.post(argv[1], data=ema)
    print(r.text)
