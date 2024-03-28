#!/usr/bin/python3
"""cript that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and
displays the body of the response (decoded in utf-8)"""


if __name__ == "__main__":
    from urllib import response, request, parse, error
    import urllib
    import sys

    try:
        values = {}
        email = sys.argv[2]
        values['email'] = email
        data = parse.urlencode(values)
        print(data)
        data = data.encode('utf-8')
        url = sys.argv[1]
        req = request.Request(url, data)
        with request.urlopen(req) as response:
            print(response.read())
    except error.URLError as e:
        print(f"URLError: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")