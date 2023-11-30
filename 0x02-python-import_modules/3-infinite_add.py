#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    na = len(sys.argv) - 1
    if na == 0:
        print("{:d}".format(na))
    else:
        i = 1
        add = 0
        while i <= na:
            add += int(sys.argv[i])
            i += 1
        print("{:d}".format(add))
