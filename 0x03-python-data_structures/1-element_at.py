#!/usr/bin/python3
def element_at(my_list, idx):
    '''
    a function that retrieves an element from a list

    parameters:
    my_list (list): list of integers
    idx: list index

    Return:
    None if index is less than 0 or greater than or equal to the
    length of the given list, otherwise the item at the given index
    '''
    if idx < 0:
        return None
    ln_ofList = len(my_list)
    if idx > ln_ofList - 1:
        return None
    return (my_list[idx])
