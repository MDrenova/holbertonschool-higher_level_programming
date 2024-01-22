#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lDigit = abs(number) % 10 * (-1 if number < 0 else 1)
if (lDigit == 0):
    print(f"Last digit of {number} is {lDigit} and is 0")
elif (lDigit > 5):
    print(f"Last digit of {number} is {lDigit} and is greater than 5")
else:
    print(f"Last digit of {number} is {lDigit} and is less than 6 and not 0")
