#!/bin/python3
def element_at(my_list, idx):
    '''
    a function that retrieves an element from a list

    parameters:
    my_list (list): list of integers
    idx: list index
    '''
    if idx < 0:
        return None
    ln_ofList = len(my_list)
    if idx > ln_ofList - 1:
        return None
    return (my_list[idx])
