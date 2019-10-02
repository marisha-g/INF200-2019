# -*- coding: utf-8 -*-
import pytest

__author__ = 'Marisha Gnanaseelan'
__email__ = 'magn@nmbu.no'


def median(data):
    """
    The following function finds the median of a dataset.
    Code inspired by original median function from Hans Ekkehard Plesser.

    :return: list
    """
    sorted_data = sorted(data)
    num_elements = len(sorted_data)

    if num_elements < 1:
        raise ValueError

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


def test_median_odd_numbers():
    """
    Test that check that the correct median is returned for lists
    with odd numbers of elements.
    """
    list_odd_numbers = [2, 4, 6, 6, 2]
    assert median(list_odd_numbers) == 4


def test_median_even_numbers():
    """
    Test that check that the correct median is returned for lists
    with even numbers of elements.
    """
    list_even_numbers = [3, 4, 5, 6]
    assert median(list_even_numbers) == 4.5


def test_median_various_orders():
    """
    Test that check that the correct median is returned for list with ordered,
    reverse-ordered and unordered elements.
    """
    list_ordered = [1, 2, 3, 4]
    list_reverse_ordered = [4, 3, 2, 1]
    list_unordered = [2, 4, 3, 1]

    assert median(list_ordered) == 2.5
    assert median(list_reverse_ordered) == 2.5
    assert median(list_unordered) == 2.5


def test_median_rasis_value_error_on_empty_list():
    """
    Test checking that requesting the median of an empty list
    raises a ValueError exception.
    """
    with pytest.raises(ValueError):  # context manager
        median([])

def test_median_original_unchanged():
    """
    Test that ensures that the median function leaves
    the original data unchanged.
    """
    data = [2, 4, 5, 8]
    _ = median(data)
    assert data == [2, 4, 5, 8]
