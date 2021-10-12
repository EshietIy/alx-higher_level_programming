#!/usr/bin/python3
'''
Defines a class BaseGeometry
'''


class BaseGeometry:
    '''BaseGeometry class
    '''

    def area(self):
        '''defines area function
        '''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''Validates value
        Args:
            name (str): the name of something
            value (int): some value that wasn't explained
        '''

        if not isinstance(value, int):
            raise TypeError('{:s} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{:s} must be greater than 0'.format(name))
