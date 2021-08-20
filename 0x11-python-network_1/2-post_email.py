#!/usr/bin/python3
""" This module posts an email """

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    from sys import argv

    url = argv[1]
    values = {'email': argv[2]}

    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        respData = response.read()
        print(respData.decode('utf-8'))
