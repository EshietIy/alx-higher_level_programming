#!/usr/bin/python3
'''
Defines a function to check to see if object inherits from a class
'''


def inherits_from(obj, a_class):
    '''Checks if object inherits from a class
    Args:
        obj: object to check.
        a_class: class to check against.
    Return:
    Returns True if it does inherit, False otherwise.
    '''
    return issubclass(obj.__class__, a_class) and (type(obj) is not a_class)
