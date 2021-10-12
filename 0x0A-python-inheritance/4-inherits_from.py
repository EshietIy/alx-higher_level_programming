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
    if isinstance(obj, a_class):
        return False
    return isinstance(obj, a_class)
