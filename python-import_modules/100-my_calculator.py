#!/usr/bin/python3
import calculator_1
import sys
if __name__ == "__main__":
    sign = "-*/+"
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    sign_arg = sys.argv[2]
    if sign_arg not in sign:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    elif sign_arg == '+':
        print("{} + {} = {}".format(a, b, calculator_1.add(a, b)))
        sys.exit(0)
    elif sign_arg == '-':
        print("{} - {} = {}".format(a, b, calculator_1.sub(a, b)))
        sys.exit(0)
    elif sign_arg == '*':
        print("{} * {} = {}".format(a, b, calculator_1.mul(a, b)))
        sys.exit(0)
    elif sign_arg == '/':
        print("{} / {} = {}".format(a, b, calculator_1.div(a, b)))
       sys. exit(0)
