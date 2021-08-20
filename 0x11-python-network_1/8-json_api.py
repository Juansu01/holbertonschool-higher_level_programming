#!/usr/bin/python3
""" This module sends a post request and displays results if found """
if __name__ == "__main__":
    import requests
    from sys import argv

    if argv[1]:
        da = {'q': argv[1]}
    else:
        da = {'q': ''}

    try:
        req = requests.post('http://0.0.0.0:5000/search_user', data=da)
        my_json = req.json()
        if 'id' in my_json or 'name' in my_json:
            print("[{}] {}".format(my_json.get('id'), my_json.get('name')))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
