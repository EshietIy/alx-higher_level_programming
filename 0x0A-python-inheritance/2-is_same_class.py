#!/usr/bin/python3
'''
Defines a function to check if the object is exactly
an instance of specified class.
'''


def is_same_class(obj, a_class):
    '''Checks if object is an exact instance of specified class.
    Args:
        obj: the object to check.
        a_class: the class to test against.
    Return:
        returns True if an exact instance, False otherwise.
    '''
    if not type(obj) is a_class:
        return False
    return True
