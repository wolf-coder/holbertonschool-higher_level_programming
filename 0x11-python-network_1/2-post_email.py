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
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print(the_page.decode("utf-8"))
