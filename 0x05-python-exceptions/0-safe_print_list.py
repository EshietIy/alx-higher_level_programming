#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for c in my_list[:x]:
            print(c, end='')
            i += 1
        print('')
    except:
        pass
    finally:
        return i
