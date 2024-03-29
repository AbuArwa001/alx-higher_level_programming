#!/usr/bin/python3
"""cript that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter, and
displays the body of the response (decoded in utf-8)"""


if __name__ == "__main__":
    import requests
    import sys

    url = 'http://0.0.0.0:5000/search_user'
    r = requests.get(url)
    if len(sys.argv) == 2:
        r = requests.post(url, data={'q': sys.argv[1]})
    else:
        r = requests.post(url, data={'q': ""})
    try:
        if r.json() == {}:
            print("No result")
        else:
            print("[{}] {}".format(r.json().get('id'), r.json().get('name')))
    except Exception:
        print("Not a valid JSON")
