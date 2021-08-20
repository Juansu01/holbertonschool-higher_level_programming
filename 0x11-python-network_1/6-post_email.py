#!/usr/bin/python3
"""This module shows a status """
if __name__ == "__main__":
    from sys import argv
    import requests
    r = requests.post(argv[1], data={'email': argv[2]})
    content = r.text
    print(content)
