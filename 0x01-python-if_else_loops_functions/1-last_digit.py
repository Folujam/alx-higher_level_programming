#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
aneg = 0
if number < 0:
    number *= -1
    aneg = 1
ld = number % 10
if aneg == 1:
    number *= -1
    ld *= -1
if ld > 5:
    print(f"last digit of {number} is {ld} and is greater than 5")
elif ld == 0:
    print(f"last digit of {number} is {ld} and is 0")
elif ld < 6 and ld != 0:
    print(f"last digit of {number} is {ld} and is less than 6 and not 0")
