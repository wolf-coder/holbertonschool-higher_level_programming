#!/usr/bin/python3
"""
handle json
"""
import requests
from sys import argv
if __name__ == "__main__":
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""
    value = {"q": q}
    url = "http://0.0.0.0:5000/search_user"
    r = requests.post(url, value)
    try:
        json_data = r.json()
        if json_data == {}:
            print("No result")
        else:
            print("[{}] {}".format(*json_data.values()))
    except Exception:
        print("Not a valid JSON")
