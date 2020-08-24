#!/usr/bin/python3
"""
"""
import requests
from sys import argv
if __name__ == "__main__":
    url = argv[1]
    REQUEST = requests.get(argv[1])
    if REQUEST.status_code >= 400:
        print(REQUEST.text)
    else:
        print("Error code: {}".format(REQUEST.status_code))
