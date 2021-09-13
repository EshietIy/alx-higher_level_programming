#!/usr/bin/python3
def no_c(my_string):
    y = ""
    for x in my_string:
        if x != 'c':
            if x == 'C':
                continue
            y += x
    return y
