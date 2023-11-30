#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    resultA = add(a, b)
    resultS = sub(a, b)
    resultM = mul(a, b)
    resultD = div(a, b)
    print("{} + {} = {}".format(a, b, resultA))
    print("{} - {} = {}".format(a, b, resultS))
    print("{} * {} = {}".format(a, b, resultM))
    print("{} / {} = {}".format(a, b, resultD))
