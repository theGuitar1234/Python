#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):

    for i in matrix:
        for j in i:
            print("{:d}".format(j), end=" ")
        print()

my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {} is {}".format(idx, element_at(my_list, idx)))