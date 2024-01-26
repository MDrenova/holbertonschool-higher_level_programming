#!/usr/bin/python3
def remove_char_at(str, n):
    str_cpy = ""
    for i in range(0, len(str)):
        # or if i != n than copy
        if i == n:
            i += 1
        str_cpy += (str[i])
    return str_cpy
