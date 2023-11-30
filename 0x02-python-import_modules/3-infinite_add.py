#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    summ = 0
    args = len(sys.argv) - 1

    for i in range(1, args + 1):
        summ += int(sys.argv[i])
    print("{}".format(summ))
