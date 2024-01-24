#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    name_list = dir(hidden_4)
    for name in name_list:
        if not name.startswith("__"):
            print("{}".format(name))

"""
Or use this simpified method
for name in sentences:
    if name[0] != "_":
        print(name)
"""
