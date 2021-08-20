#!/usr/bin/python3
"""This is some documentation yes """
if __name__ == "__main__":
    import requests
    from sys import argv

    owner = argv[2]
    repo = argv[1]
    query_url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    r = requests.get(query_url)
    d = r.json()
    try:
        for commit in d:
            for val in range(0, 10):
                print(
                    "{}: {}".format(
                        d[val]["sha"], d[val]["commit"]["author"]["name"]))
            break
    except:
        pass
