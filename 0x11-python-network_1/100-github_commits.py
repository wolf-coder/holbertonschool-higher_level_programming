#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to display last 10 commits.
"""


if __name__ == '__main__':
    import sys
    import requests
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = '/'.join(["https://api.github.com/repos",
                    repo,
                    owner,
                    "commits"])
    Resp = requests.get(url)
    Commits = Resp.json()[:10]
    for i in Commits:
        elem = i['sha']
        author = i['commit']['author']['name']
        print('{}: {}'.format(elem, author))
