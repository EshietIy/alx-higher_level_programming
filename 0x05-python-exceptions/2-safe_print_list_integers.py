#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    for itm in range(x):
        try:
            print("{:d}".format(my_list[itm]), end='')
            i += 1
        except ValueError:
            continue
        except TypeError:
            continue
    print('')
    return (i)
