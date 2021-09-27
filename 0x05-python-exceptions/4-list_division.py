#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    ln1 = len(my_list_1)
    ln2 = len(my_list_2)
    new_list = []
    for x in range(list_length):
        try:
            new_list.append(my_list_1[x] / my_list_2[x])
        except TypeError:
            new_list.append(0)
            print("Wrong type")
        except ZeroDivisionError:
            new_list.append(0)
            print("division by 0")
        except IndexError:
            new_list.append(0)
            print("out of range")
        finally:
            if list_length == len(new_list):
                return new_list
