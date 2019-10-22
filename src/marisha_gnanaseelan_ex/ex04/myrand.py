# -*- coding: utf-8 -*-

__author__ = 'Marisha Gnanaseelan'
__email__ = 'magn@nmbu.no'


class LCGRand:
    """
    Implements a linear congruential generator (LCG),
    which generates numbers according to the following equation:
    r[n+1] = a * r[n] mod m
    """
    a = 7 ** 5
    m = 2 ** 31 - 1

    def __init__(self, seed):
        """
        :param seed: random number generator
        """
        self._seed = seed

    def rand(self):
        """
        :return: next random number
        """
        self._seed = (LCGRand.a * self._seed) % LCGRand.m
        return self._seed


class ListRand:
    """
    Is based on a list of numbers. The constructor takes a list of numbers,
    and rand() returns the first number from that list when it is called
    for the first time, the second number when called the second time, etc.
    It shall raise a RuntimeError if rand() is called after the last number
    in the list has been delivered.
    """
    def __init__(self, numbers):
        """
        :param numbers: list of numbers
        """
        self.numbers = numbers
        self.next = 0

    def rand(self):
        """
        :return: next random number
        """
        if self.next >= len(self.numbers):
            raise RuntimeError('Last number in the list has been delivered.')

        next_random_number = self.numbers[self.next]
        self.next += 1
        return next_random_number


if __name__ == "__main__":
    lst = ListRand([23, 4, 65, 32, 12])
    lcg = LCGRand(245)

    print("Drawing random numbers")
    print("ListRand", "LCGRand")
    for i in range(5):
        print(lst.rand(), lcg.rand())
