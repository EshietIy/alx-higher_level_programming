#!/usr/bin/python3
""" square module / task 10 """

from .rectangle import Rectangle


class Square(Rectangle):
    '''Square class that inherits from Rectangle
    '''

    def __init__(self, size, x=0, y=0, id=None):
        '''Initializes the Square object
        Args:
            size (int): size of the square
            x (int): position on the x axis
            y (int): position on the y axis
            id (int): the id of the object
        '''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """retrieves the size => width attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """set the new value to the size attribute (width and height)"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update the instance atttributes from
        the arguments passed in a strict order
        or from the kwargs
        """
        i = 0
        attributes = ['id', 'size', 'x', 'y']
        if len(args) > 0:
            for attr in attributes:
                if i > len(args) - 1:
                    break
                setattr(self, attr, args[i])
                i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """
        Returns a string representation of a square
        """
        return ("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size))

    def to_dictionary(self):
        """ a function that returns the dict
        representation of an object
        """
        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}
