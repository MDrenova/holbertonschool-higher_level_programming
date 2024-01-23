#!/usr/bin/python3
import 7-islower.py


def uppercase(str):
    strCpy = ''
    for char in str:
        if islower(char):
            strCpy += chr(ord(char) - 32)
        else:
            strCpy += char
    print(strCpy)
