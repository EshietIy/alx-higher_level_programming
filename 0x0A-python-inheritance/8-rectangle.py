#!/usr/bin/python3
'''
Defines two classes BaseGeometry and Rectangle
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' Rectangle class inherits from BaseGeometry
    '''

    def __init__(self, width, height):
        """Initializes a Rectangle object.
        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
