#!/usr/bin/python3
"""Sends a request to a given URL and displays the response body.

Usage: ./4-hbtn_status.py
"""

if __name__ == "__main__":

    import requests
    import sys

    url = sys.argv[1]
    request = requests.get(url)
    try:
        print(request.headers['X-Request-Id'])
    except Exception:
        pass
