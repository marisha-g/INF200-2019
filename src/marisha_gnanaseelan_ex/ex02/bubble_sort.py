# -*- coding: utf-8 -*-

__author__ = 'Marisha Gnanaseelan'
__email__ = 'magn@nmbu.no'


def bubble_sort(data):
    """
    A simple sorting algorithm that returns the input data in ascending order.

    :return: list
    """
    new_data = list(data)
    length_lst = len(new_data)

    for i in range(length_lst):
        for k in range(length_lst-i-1):
            if new_data[k + 1] < new_data[k]:
                new_data[k + 1], new_data[k] = new_data[k], new_data[k + 1]
    return new_data


if __name__ == "__main__":

    for data in ((),
                 (1,),
                 (1, 3, 8, 12),
                 (12, 8, 3, 1),
                 (8, 3, 12, 1)):
        print('{!s:>15} --> {!s:>15}'.format(data, bubble_sort(data)))
