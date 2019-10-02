# -*- coding: utf-8 -*-

__author__ = 'Marisha Gnanaseelan'
__email__ = 'magn@nmbu.no'


def median(data):
    """
    The following function finds the median of a dataset.

    :return: list
    """
    sorted_data = sorted(data)
    num_elements = len(sorted_data)

    if num_elements % 2 == 1:
        return sorted_data[num_elements // 2]
    else:
        return (
            sorted_data[num_elements // 2 - 1]
            + sorted_data[num_elements // 2]
        ) / 2


def test_median_of_singleton():
    """
    Test that the median function returns the correct value
    for a one-element list.
    """
    assert median([4]) == 4
