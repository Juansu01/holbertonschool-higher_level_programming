#!/usr/bin/python3
if __name__ == "__main__":
    import request
    from sys import argv
    from requests.exceptions import HTTPError
    url = argv[1]
    r = requests.get(url)
    if r.status_code > 400:
        print('Error code: {}'.format(r.status_code))
    else:
        print(r.text)
