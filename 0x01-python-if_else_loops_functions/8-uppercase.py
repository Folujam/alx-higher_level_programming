#!/usr/bin/python3
def uppercase(str):
    result = ""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            d = chr(ord(c) - 32)
            result += d
        else:
            result += c
    print("{}".format(result))
