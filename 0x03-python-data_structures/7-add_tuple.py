#!/usr/bin/python3
def tuple_check(c=()):
    length = len(c)
    if length == 0:
        return (0, 0)
    if length == 1:
        return (c[0], 0)
    return c


def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_check(tuple_a)
    b = tuple_check(tuple_b)
    return (tuple(map(lambda x, y: x + y, a[:2], b[:2])))
