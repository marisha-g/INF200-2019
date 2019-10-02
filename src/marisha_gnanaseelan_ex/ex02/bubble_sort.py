# -*- coding: utf-8 -*-

__author__ = 'Marisha Gnanaseelan'
__email__ = 'magn@nmbu.no'


def bubble_sort(data):
    """
    A simple sorting algorithm that returns the input data in ascending order.

    :return: list
    """
    lst_data = list(data)
    length_lst = len(lst_data)

    for i in range(length_lst):
        for j in range(length_lst-i-1):
            if lst_data[j + 1] < lst_data[j]:
                lst_data[j + 1], lst_data[j] = lst_data[j], lst_data[j + 1]
    return lst_data


if __name__ == "__main__":

    for data in ((),
                 (1,),
                 (1, 3, 8, 12),
                 (12, 8, 3, 1),
                 (8, 3, 12, 1)):
        print('{!s:>15} --> {!s:>15}'.format(data, bubble_sort(data)))
