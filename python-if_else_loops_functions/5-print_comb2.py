#!/usr/bin/python3
for nr in range(0, 100):
    if (nr < 99):
        print("0{}, ".format(nr) if nr < 10 else "{}, ".format(nr), end="")
    else:
        print("{}".format(nr))
