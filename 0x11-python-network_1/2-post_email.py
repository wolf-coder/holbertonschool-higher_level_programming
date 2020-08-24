#!/usr/bin/python3
"""
 POST an email #0
"""
from sys import argv
from urllib import request
import urllib.parse

if __name__ == "__main__":
    url = argv[1]
    values = {"email": argv[2]}
    DATA = urllib.parse.urlencode(values)
    DATA = DATA.encode('ascii')
    req = urllib.request.Request(url, DATA)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print(sthe_page.decode("utf-8"))
