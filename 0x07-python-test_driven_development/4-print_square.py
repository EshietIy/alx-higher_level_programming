#!/usr/bin/python3
"""
A Print Squar model
This module prints a square with '#'
"""


def print_square(size):
    """A function that prints a square
    with a "#" character

    Args:
        size: (int)

    Return:
        None.
    """
    if not type(size) is int:
        raise TypeError("size must be an integer")

    elif size < 0:
        raise ValueError("size must be >= 0")

    for x in range(size):
        print("#" * size)
