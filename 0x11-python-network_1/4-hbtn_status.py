#!/usr/bin/python3
"""This module shows a status """
if __name__ == "__main__":
    import requests
    resp = requests.get('https://intranet.hbtn.io/status')
    content = resp.text
    print('Body response:')
    print('\t- type: {}'.format(type(content)))
    print('\t- content: {}'.format(content))
