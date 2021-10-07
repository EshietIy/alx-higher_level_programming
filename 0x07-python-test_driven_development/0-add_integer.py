#!/usr/bin/python3
"""
This module defines 'add_integer'

The function return the sum of 'a' and 'b'
"""


def add_integer(a, b=98):
    """adds a and b

    Args:
        a (int or float)
        b (int or float): defult to 98.

    Raises:
         TypeError: a and b must be integer

    Returns:
         int: sum of a nad b
    """
    if not type(a) in [int, float]:
        raise TypeError("a must be an integer")
    if not type(b) in [int, float]:
                raise TypeError("b must be an integer")
    return int(a) + int(b)
