#!/usr/bin/python3
"""
6. POST an email #1
"""
from sys import argv
import requests
if __name__ == "__main__":
    url = argv[1]
    values = {"email": argv[2]}

    Request = requests.post(url, values)
    print(Request.text)
