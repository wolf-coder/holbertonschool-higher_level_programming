#!/usr/bin/python3

"""
 4. What's my status? 
"""

import requests
if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    Request = requests.get(url)
    Request = Request.text
    print("Body response:")
    print("\t- type: {}".format(type(Request)))
    print("\t- content: {}".format(Request))
