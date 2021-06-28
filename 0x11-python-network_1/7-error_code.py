#!/usr/bin/python3
"""
Handling error code
"""
import requests
from sys import argv
if __name__ == "__main__":
    url = argv[1]
    Resp = requests.get(argv[1])
    if Resp.status_code <= 400:
        print(Resp.text)
    else:
        print("Error code: {}".format(Resp.status_code))
