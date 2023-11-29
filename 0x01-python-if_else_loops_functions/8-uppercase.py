#!/usr/bin/python3
def pr(c):
    print("{:s}".format(c), end="")
def uppercase(str):
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            i = chr(ord(i) - 32)
            pr(i)
        else:
            pr(i)
    print()
