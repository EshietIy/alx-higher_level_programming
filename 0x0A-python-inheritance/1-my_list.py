#!/usr/bin/python3
'''
This module defines a class mylist
'''


class MyList(List):
    '''custom list class that inherits from lists

    '''

    def print_sorted(self):
        ''' print the sorted version of the list

        '''
        print(sorted(self))
