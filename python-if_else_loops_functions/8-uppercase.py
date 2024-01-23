#!/usr/bin/python3
def uppercase(str):
    strCpy = ''
    for char in str:
        if 'a' <= char <= 'z':
            strCpy += chr(ord(char) - 32)
        else:
            strCpy += char
    print(strCpy)
