#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = len(sys.argv) - 1
    arg = "arguments"
    if args == 1:
        arg = "argument"

    print("{} {}:".format(args, arg))

    for i in range(1,args + 1):
        print("{}: {}".format(i, sys.argv[i]))
