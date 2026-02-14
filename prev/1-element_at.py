#!/usr/bin/python3


def element_at(my_list, idx):

    if idx < 0:
        return None
    elif idx >= len(my_list):
        return None
    return my_list[idx]

my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {} is {}".format(idx, element_at(my_list, idx)))