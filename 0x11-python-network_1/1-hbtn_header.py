#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and
    displays the value of the X-Request-Id"""


if __name__ == "__main__":
    from urllib import response, request
    import sys

    req = request.Request(sys.argv[1])
    with request.urlopen(req) as response:
        print(response.info().get('X-Request-Id'))
