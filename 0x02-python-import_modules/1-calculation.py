#!/usr/bin/python3
from calculation_1 import add, sub, mul, div
a = 10
b = 5
resultA = add(a, b)
resultS = sub(a, b)
resultM = mul(a, b)
resultD = div(a, b)
if __name__ == "__main__":
    print(a, "+", b, "=", resultA)
    print(a, "-", b, "=", resultS)
    print(a, "*", b, "=", resultM)
    print(a, "/", b, "=", resultD)
