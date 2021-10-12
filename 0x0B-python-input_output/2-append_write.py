#!/usr/bin/python3
'''
a module that defines a function
that appends to file
'''


def append_write(filename="", text=""):
    """"append write"""
    with open(filename, mode="a", encoding="utf-8") as fd:
        fd.write(text)
    return len(text)
