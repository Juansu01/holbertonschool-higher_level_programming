#!/usr/bin/python3
"""This module shows a status """
if __name__ == "__main__":
    from sys import argv
    import requests
    resp = requests.get(argv[1])
    get_id = resp.headers.get('X-Request-Id')
    print(get_id)
