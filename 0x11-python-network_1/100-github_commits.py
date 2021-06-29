#!/usr/bin/python3
"""Python script that takes 2 arguments in order to display last 10 commits.
"""


if __name__ == '__main__':
    import sys
    import requests
    url = "https://api.github.com/repos/{}/{}/commits".\
        format(sys.argv[1], sys.argv[2])
    Resp = requests.get(url)
    Commits_10 = Resp.json()[:10]
    for i in Commits_10:
        elem = i['sha']
        author = i['commit']['author']['name']
        print('{}: {}'.format(elem, author))
