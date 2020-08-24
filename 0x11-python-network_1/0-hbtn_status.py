#!/usr/bin/python3
"""[fetching  https://intranet.hbtn.io/status]
"""
from urllib import request
if __name__ == "__main__":
    with request.urlopen('https://intranet.hbtn.io/status') as Resp:
        htm = Resp.read()
        print('Body response:')
        print("\t- type: {}".format(type(htm)))
        print("\t- content: {}".format(htm))
        print("\t- utf8 content: {}".format(htm.decode('utf-8')))
