#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1 as cal

    args = len(sys.argv)

    if args != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    op = sys.argv[2]
    if op not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    res = 0

    if op == "+":
        res = cal.add(a, b)
    if op == "-":
        res = cal.sub(a, b)
    if op == "*":
        res = cal.mul(a, b)
    if op == "/":
        res = cal.div(a, b)

    print("{} {} {} = {}".format(a, op, b, res))
