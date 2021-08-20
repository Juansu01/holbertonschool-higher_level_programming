#!/usr/bin/python3
""" This module sends a get request to the github api """
if __name__ == "__main__":
    import requests
    from sys import argv
    user = argv[1]
    pwd = argv[2]
    r = requests.get("https://api.github.com/user", auth=(user, pwd))
    my_json = r.json()
    print(my_json.get('id'))
