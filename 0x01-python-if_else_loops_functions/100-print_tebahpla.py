#!/usr/bin/python3
for i in range(ord('z'), ord('A') - 1, -1):
    print(chr(i) if 1 % 2 == 0 else chr(i).upper(), end='')
    