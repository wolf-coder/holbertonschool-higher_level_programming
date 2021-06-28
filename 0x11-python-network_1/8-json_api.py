#!/usr/bin/python3
"""
handle json
"""
import requests
import sys
if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    value = {"q": q}
    url = "http://0.0.0.0:5000/search_user"
    # url = "http://34.227.194.97:50029/search_user"
    r = requests.post(url, value)
    try:
        json_data = r.json()
        if json_data == {}:
            print("No result")
        else:
            print("[{}] {}".format(*json_data.values()))
    except Exception:
        print("Not a valid JSON")
