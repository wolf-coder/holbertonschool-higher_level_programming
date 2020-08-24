#!/usr/bin/python3
"""
"""
import requests
from sys import argv
if __name__ == "__main__":
    url = argv[1]
    Request = requests.get(argv[1])
    if Request.status_code <= 400:
        print(Request.text)
    else:
        print("Error code: {}".format(Request.status_code))
