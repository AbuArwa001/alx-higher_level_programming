#!/usr/bin/python3
"""Sends a request to a given URL and displays the response body.

Usage: ./4-hbtn_status.py
"""


if __name__ == "__main__":

    import requests

    url = 'https://alx-intranet.hbtn.io/status'
    req = requests.get(url)
    print(f"Body response:")
    print(f"\t- type: {type(req.text)}")
    print(f"\t- content: {req.text}")
