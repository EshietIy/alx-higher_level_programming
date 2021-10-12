#!/usr/bin/python3
'''a module that define a function that
prints to stdout
'''


def read_file(filename=""):
    '''a function that prints text file to stdout
    Args:
        filename: (str) name or path to file
    Return:
        None
    '''
    with open(filename, encoding='utf8') as f:
        for line in f:
            print(line, end='')
