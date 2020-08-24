#!/usr/bin/python3
"""
Response header value #1
"""
from sys import argv
import requests
if __name__ == "__main__":
    Request = requests.get(argv[1])
    print(Request.headers.get('X-Request-Id'))
