#!/usr/bin/python3
"""cript that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter, and
displays the body of the response (decoded in utf-8)"""


if __name__ == "__main__":
    import requests
    import sys

    values = {}
    email = sys.argv[2]
    values['email'] = email
    url = sys.argv[1]
    response = requests.post(url, data=values)
    print(response.text)
