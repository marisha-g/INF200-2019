# -*- coding: utf-8 -*-

__author__ = 'Marisha Gnanaseelan'
__email__ = 'magn@nmbu.no'


def char_counts(textfilename):
    """
    This function opens and reads a given file with utf-8 encoding.
    It also counts how often each character code (0–255) occurs in the string
    and return the result as a list or tuple.

    :return: list
    """

    with open(textfilename, 'r', encoding='utf-8') as read_file:
        read_file = read_file.read()

    result = [0] * 256  # empty list with zeros
    for char in read_file:
        result[ord(char)] += 1  # converting the characters to integers
    return result


if __name__ == '__main__':

    filename = 'file_stats.py'
    frequencies = char_counts(filename)
    for code in range(256):
        if frequencies[code] > 0:
            character = ''
            if code >= 32:
                character = chr(code)

            print(
                '{:3}{:>4}{:6}'.format(
                    code, character, frequencies[code]
                )
            )
