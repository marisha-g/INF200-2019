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
    frequencies = {}
    txt_lower = txt.lower()

    for i in txt_lower:
        keys = frequencies.keys()
        if i in keys:
            frequencies[i] += 1
        else:
            frequencies[i] = 1
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
