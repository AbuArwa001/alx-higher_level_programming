#!/usr/bin/python3
"""Sends a request to a given URL and displays the response body.

Usage: ./3-error_code.py <URL>
  - Handles HTTP errors.
"""
import sys
from urllib import error, request


if __name__ == "__main__":
    url = sys.argv[1]

    req = request.Request(url)
    try:
        with request.urlopen(req) as response:
            print(response.read().decode("utf-8"))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
