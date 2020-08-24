#!/usr/bin/python3
"""
"""
import requests
from syss import argv
if __name__ == "__main__":
    url = argv[1]
    req = requests.get(argv[1])
    if req.status_code <= 400:
        print(req.text)
    else:
        print("Error code: {}".format(req.status_code))
