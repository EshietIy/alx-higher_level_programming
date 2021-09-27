#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    ln1 = len(my_list_1)
    ln2 = len(my_list_2)
    new_list = []
    for x in range(list_length):
        result = 0
        try:
            result = my_list_1[x] / my_list_2[x]
        except TypeError:
            print("Wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(result)
    return new_list
