#!usr/bin/python3
"""
A module that prints the first name and last name
"""


def say_my_name(first_name, last_name=""):
    """A function that prints the first name and last name

    Args:
        first_name: (str)
        last_name: (str)

    Returns:
        NOne
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
