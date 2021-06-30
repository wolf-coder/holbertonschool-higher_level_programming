#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to display last 10 commits.
"""

if __name__ == '__main__':
    import sys
    import requests
    repo = sys.argv[1]
    owner = sys.argv[2]
    info = owner + "/" + repo
    r = requests.get("https://api.github.com/repos/" + info + "/commits")
    cmt = r.json()[:10]
    for i in cmt:
        elem = i['sha']
        author = i['commit']['author']['name']
        print('{}: {}'.format(elem, author))
