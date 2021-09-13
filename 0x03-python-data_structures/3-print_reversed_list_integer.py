#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    '''
    a function that prints all integers of a list in reverse
    
    Parameters:
    my_list (list): list parameter
    '''
    for x in range(-1, ((len(my_list) + 1) * -1), -1):
        print(my_list[x])
