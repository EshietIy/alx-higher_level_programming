#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_set = set(my_list)
    sum_of_list = 0
    for x in new_set:
        sum_of_list += x
    return sum_of_list
    
