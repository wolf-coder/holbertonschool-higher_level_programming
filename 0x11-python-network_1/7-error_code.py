#!/usr/bin/python3
"""
"""
from sys import argv
from  requests import get
if __name__ == "__main__":
    url = argv[1]
    Request = get(argv[1])
    if Request.status_code <= 400:
        print(Request.text)
    else:
        print("Error code: {}".format(Request.status_code))
