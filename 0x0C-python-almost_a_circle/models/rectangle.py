#!/usr/bin/python3
'''
this module defines a rectangle object
'''
from models.base import Base


class Rectangle(Base):
    """

    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Inizialization"""
        self.verify_int(width, height, x, y)
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ returns the width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """ set the width property"""
        self.verify_int(width=value)
        self.__width = value

    @property
    def height(self):
        """ returns the height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """ set the height property"""
        self.verify_int(height=value)
        self.__height = value

    @property
    def x(self):
        """ returns the x value"""
        return self.__x

    @x.setter
    def x(self, value):
        """ set the x property"""
        self.verify_int(x=value)
        self.__x = value

    @property
    def y(self):
        """ returns the y value"""
        return self.__y

    @y.setter
    def y(self, value):
        """ set the y property"""
        self.verify_int(y=value)
        self.__y = value

    def verify_int(self, width=None, height=None, x=None, y=None):
        """a function that verifies
        if width and height are int
        Args:
           width: (int)
           height: (int)
           x: (int)
           y: (int)
        Return: None
        """
        w = ('width', width) if width is not None else None
        h = ('height', height) if height is not None else None
        X = ('x', x) if x is not None else None
        Y = ('y', y) if y is not None else None

        if w is not None:
            if not type(w[1]) is int:
                raise TypeError("{} must be an integer".format(w[0]))
            if w[1] <= 0:
                raise ValueError("{} must be > 0".format(w[0]))

        if h is not None:
            if not type(h[1]) is int:
                raise TypeError("{} must be an integer".format(h[0]))
            if h[1] <= 0:
                raise ValueError("{} must be > 0".format(h[0]))

        if X is not None:
            if not type(X[1]) is int:
                raise TypeError("{} must be an integer".format(X[0]))
            if X[1] < 0:
                raise ValueError("{} must be >= 0".format(X[0]))

        if Y is not None:
            if not type(Y[1]) is int:
                raise TypeError("{} must be an integer".format(Y[0]))
            if Y[1] < 0:
                raise ValueError("{} must be >= 0".format(Y[0]))

    def area(self):
        """a function that calculate area of
        a rectangle
        """
        return self.height * self.width

    def display(self):
        """ this fuction prints the instance of
        of the rectangle
        """
        y = 0
        while y < self.y:
            print()
            y += 1
        for h in range(self.height):
            x = 0
            while x < self.x:
                print(' ', end="")
                x += 1
            for w in range(self.width):
                print("#", end='')
            print()

    def __str__(self):
        """str representaion of rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """updats class variables using *args"""
        atr = ['id', 'width', 'height', 'x', 'y']
        i = 0
        lof_args = len(args)

        if lof_args > 0:
            while i < lof_args:
                setattr(self, atr[i], args[i])
                i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ a function that gives adictinary
        representation of a rectangle
        """
        return {
            'x': self.x, 'y': self.y, 'id': self.id,
            'height': self.height, 'width': self.width}
