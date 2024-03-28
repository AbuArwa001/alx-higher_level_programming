#!/usr/bin/python3
from urllib import request

url = 'https://alx-intranet.hbtn.io/status'
req = request.Request(url)

with request.urlopen(req) as response:
    red = response.read()
    print(f"Body response.info: {response.info()['Content-Type']}")
    print(f"Body response:")
    print(f"\t- type: {type(red)}")
    content_type = response.info().get('Content-Type')
    if content_type and 'charset=utf-8' in content_type.lower():
        print(f"\t- content: OK")
    print(f"\t- utf8 content: {response.reason}")
