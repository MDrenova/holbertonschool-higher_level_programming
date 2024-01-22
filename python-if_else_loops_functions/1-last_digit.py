import random
number = random.randint(-10000, 10000)
lastDigit = abs(number) % 10 * (-1 if number < 0 else 1)
if (lastDigit == 0):
    print(f"Last digit of {number} is {lastDigit} and is 0")
elif (number > 5):
    print(f"Last digit of {number} is {lastDigit} and is greater than 5")
else:
    print(f"Last digit of {number} is {lastDigit} and is less than 6 and not 0")
