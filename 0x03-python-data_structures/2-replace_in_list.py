#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    '''
    a function that replaces an element of a list
    at a specific point

    Parameters:
    my_list (list): list of element
    idx (int): index of list
    element (int): element to replace

    Return:
    original list if idx is negative or out of range
    '''
    if idx < 0:
        return my_list
    ln_ofList = len(my_list)
    if idx > ln_ofList - 1:
        return my_list
    my_list[idx] = element
    return my_list
