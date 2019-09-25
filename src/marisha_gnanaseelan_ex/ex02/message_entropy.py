# -*- coding: utf-8 -*-

from math import log2

__author__ = 'Marisha Gnanaseelan'
__email__ = 'magn@nmbu.no'


def letter_freq(txt):
    """
    This program prints the number of times each letter, digit or symbol
    appears in the string passed to letter_freq().

    :return: dict
    """
    frequencies = {}  # empty dictionary
    txt_lower = txt.lower()  # all letters are made into lowercase letters

    for i in txt_lower:
        keys = frequencies.keys()  # list of all the keys in the dictionary
        if i in keys:  # checks if the letter, digit or symbol is in the dictionary keys
            frequencies[i] += 1  # if the if-statement is true then the value to the corresponding key is added by 1
        else:
            frequencies[i] = 1  # if the if-statement is false then the value to the corresponding key is 1
    return frequencies


def entropy(message):
    """
    Returns the entropy calculated according to the equation for entropy.

    :return: float
    """
    message = letter_freq(message)
    n = sum(message.values())
    h = 0
    for n_i in message.values():
        p_i = n_i / n
        h += -p_i * log2(p_i)
    return h


if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))
