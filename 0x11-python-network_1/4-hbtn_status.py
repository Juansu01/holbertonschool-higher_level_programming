#!/usr/bin/python3
"""This module shows a status """
if __name__ == "__main__":
    import urllib.request
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        resp = response.read()
        decoded = resp.decode('UTF-8')
        print('Body response:')
        print('\t- type: {}'.format(type(decoded)))
        print('\t- content: {}'.format(decoded))
