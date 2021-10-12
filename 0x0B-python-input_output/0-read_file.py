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
    f_list = []
    with open(filename, encoding='utf8') as f:
        f_list = f.readlines()
        for line in f_list:
            print(line)
