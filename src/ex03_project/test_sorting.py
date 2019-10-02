# -*- coding: utf-8 -*-

__author__ = 'Marisha Gnanaseelan'
__email__ = 'magn@nmbu.no'


def bubble_sort(data):
    """
    A simple sorting algorithm that returns the input data in ascending order.

    :return: list
    """
    sorted_data = list(data)
    length_lst = len(sorted_data)

    for i in range(length_lst):
        for j in range(length_lst-i-1):
            if sorted_data[j + 1] < sorted_data[j]:
                sorted_data[j + 1], sorted_data[j] = sorted_data[j], sorted_data[j + 1]
    return sorted_data


def test_empty():
    """Test that the sorting function works for empty list"""
    empty_list = []
    assert empty_list == bubble_sort(empty_list)


def test_single():
    """Test that the sorting function works for single-element list"""
    single_element_list = [1]
    assert single_element_list == bubble_sort(single_element_list)


def test_sorted_is_not_original():
    """
    Test that the sorting function returns a new object.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now sorted_data shall be a different object than data,
    not just another name for the same object.
    """
    data = [3, 2, 1]
    sorted_data = bubble_sort(data)
    assert sorted_data != data


def test_original_unchanged():
    """
    Test that sorting leaves the original data unchanged.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now data shall still contain [3, 2, 1].
    """
    data = [3, 2, 1]
    sorted_data = bubble_sort(data)
    assert data == [3, 2, 1]


def test_sort_sorted():
    """Test that sorting works on sorted data."""
    sorted_data = [1, 2, 3]
    sort_sorted_data = bubble_sort(sorted_data)
    assert sorted_data == sort_sorted_data


def test_sort_reversed():
    """Test that sorting works on reverse-sorted data."""
    reversed_data = [6, 4, 2]
    sorted_data = bubble_sort(reversed_data)
    assert sorted_data == [2, 4, 6]


def test_sort_all_equal():
    """Test that sorting handles data with identical elements."""
    identical_elements = [1, 1, 1]
    sorted_data = bubble_sort(identical_elements)
    assert sorted_data == [1, 1, 1]


def test_sorting():
    """
    Test sorting for various test cases.

    This test case should test sorting of a range of data sets and
    ensure that they are sorted correctly. These could be lists of
    numbers of different length or lists of strings.
    """
    list_of_strings = ['a', 'n', 'f']
    list_of_int_1 = [9, 6]
    list_of_int_2 = [8, 3, 5, 6, 7, 9, 2, 2]
    list_of_float = [3.2, 1.2, 1.4, 5.6]

    assert bubble_sort(list_of_strings) == ['a', 'f', 'n']
    assert bubble_sort(list_of_int_1) == [6, 9]
    assert bubble_sort(list_of_int_2) == [2, 2, 3, 5, 6, 7, 8, 9]
    assert bubble_sort(list_of_float) == [1.2, 1.4, 3.2, 5.6]
