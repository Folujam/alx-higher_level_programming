#!/usr/bin/python3
import calculation_1
a = 10
b = 5
resultA = calculation_1.add(a, b)
resultS = calculation_1.sub(a, b)
resultM = calculation_1.mul(a, b)
resultD = calculation_1.div(a, b)
if __name__ == "__main__":
    print("{} + {} = {}".format(a, b, resultA))
    print("{} - {} = {}".format(a, b, resultS))
    print("{} * {} = {}".format(a, b, resultM))
    print("{} / {} = {}".format(a, b, resultD))
