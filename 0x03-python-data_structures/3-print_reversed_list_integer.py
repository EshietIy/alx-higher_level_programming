#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    '''
    a function that prints all integers of a list in reverse

    Parameters:
    my_list (list): list parameter
    '''
    if not my_list:
        return
    for i in reversed(my_list):
        print("{:d}".format(i))
