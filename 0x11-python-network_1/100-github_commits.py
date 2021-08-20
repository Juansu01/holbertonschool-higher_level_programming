#!/usr/bin/python3
"""This is some documentation yes """
import requests
from sys import argv

owner = argv[1]
repo = argv[2]
query_url = f"https://api.github.com/repos/{owner}/{repo}/commits"
r = requests.get(query_url)
commits = r.json()
for commit in commits:
    for val in range(0, 10):
        print(
            "{}: {}".format(
                commits[val]["sha"], commits[val]["commit"]["author"]["name"]))
    break
