#!/usr/bin/python3
"""[Response header value #0 ]
"""
from sys import argv
from urllib import request

if __name__ == "__main__":
    with request.urlopen(argv[1]) as Res:
        print(Res.headers.get('X-Request-Id'))
