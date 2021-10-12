#!/usr/bin/python3
'''
A module that defines a fuction
that returns true if an object is an instance of a class
'''


def is_kind_of_class(obj, a_class):
    ''' this function returns True if the object is sn instsnce
    of class that it inherits from or object
    Args:
        obj: object to check
        a_class: class to check against

    Returns:
        True if its an instance or False
    '''
    return isinstance(obj, a_class)
