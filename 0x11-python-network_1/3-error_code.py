#!/usr/bin/python3
"""
3. Error code #0
"""
from sys import argv
import urllib.parse
from urllib import request
if __name__ == "__main__":
    url = argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode())
    except urllib.error.URLError as b:
        print("Error code: {}".format(b.code))
