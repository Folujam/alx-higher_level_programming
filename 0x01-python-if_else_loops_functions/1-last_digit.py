#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = abs(number)
ld = num % 10
sign = -1 if number < 0 else 1
ld = ld * sign
if ld > 5:
    print(f"last digit of {number} is {ld} and is greater than 5")
elif ld == 0:
    print(f"last digit of {number} is {ld} and is 0")
elif ld < 6 and ld != 0:
    print(f"last digit of {number} is {ld} and is less than 6 and not 0")
