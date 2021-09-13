#!/usr/bin/python3
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


def divisible_by_2(my_list=[]):
    return list(map(is_even, my_list))
