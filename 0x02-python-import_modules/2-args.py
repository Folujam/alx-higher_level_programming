#!/usr/bin/python3
import sys
if __name__ == "__main__":
    numargs = len(sys.argv) - 1
    if numargs > 1:
        print(f"{numargs} arguments:")
    elif numargs == 1:
        print(f"{numargs} argument:")
    elif numargs == 0:
        print(f"{numargs} arguments.")
    for i in range(1, numargs + 1):
        print(f"{i}: {sys.argv[i]}")