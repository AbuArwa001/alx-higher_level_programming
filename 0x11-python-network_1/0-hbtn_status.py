#!/usr/bin/python3
"""Module that fetches https://alx-intranet.hbtn.io/status"""


if __name__ == "__main__":
    from urllib import request

    url = 'https://alx-intranet.hbtn.io/status'
    req = request.Request(url)
    with request.urlopen(req) as response:
        red = response.read()
        print(f"Body response:")
        print(f"\t- type: {type(red)}")
        print(f"\t- content: {red}")
        print("\t- utf8 content: {}".format(red.decode("utf-8")))
