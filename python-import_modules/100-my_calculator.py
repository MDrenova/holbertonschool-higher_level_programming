#!/usr/bin/python3
import calculator_1
import sys
if __name__ == "__main__":
    sign = "-*/+"
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        print(1)
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    sign_arg = sys.argv[2]
    if sign_arg not in sign:
        print("Unknown operator. Available operators: +, -, * and /")
        print(1)
        sys.exit(1)
    elif sign_arg == '+':
        print("{} + {} = {}".format(a, b, calculator_1.add(a, b)))
        print(0)
        sys.exit(0)
    elif sign_arg == '-':
        print("{} - {} = {}".format(a, b, calculator_1.sub(a, b)))
        print(0)
        exit()
    elif sign_arg == '*':
        print("{} * {} = {}".format(a, b, calculator_1.mul(a, b)))
        print(0)
        exit()
    elif sign_arg == '/':
        print("{} / {} = {}".format(a, b, calculator_1.div(a, b)))
        print(0)
        exit()
