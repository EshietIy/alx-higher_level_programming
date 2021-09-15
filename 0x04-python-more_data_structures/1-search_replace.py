#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for x, y in enumerate(new_list):
        if y == search:
            new_list[x] = replace
        else:
            continue
    return new_list
            
