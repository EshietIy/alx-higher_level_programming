#!/usr/bin/python3
def uppercase(str):
    upper = ""
    for i in str:
        c = ord(i)
        if ord('a') <= c <= ord('z'):
            c = c - 32
        upper += chr(c)
    print("{}".format(upper))
