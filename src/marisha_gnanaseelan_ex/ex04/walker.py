# -*- coding: utf-8 -*-

import random

__author__ = 'Marisha Gnanaseelan'
__email__ = 'magn@nmbu.no'


class Walker:
    def __init__(self, start_pos, home):
        """
        :param start_pos: initial position of the walker
        :param home: position of the walker´s home
        """
        self.x = start_pos
        self.home = home
        self.steps = 0

    def move(self):
        """
        :return: steps to the left(x-1) or right(x+1) with equal probability
        """
        self.x += 2 * random.uniform(0, 1) - 1
        self.steps += 1

    def is_at_home(self):
        """
        :return: true if walker is at home
        """
        return self.x == self.home

    def get_position(self):
        """
        :return: current position
        """
        return self.x

    def get_steps(self):
        """
        :return: steps taken
        """
        return self.steps


def start_to_home(start_pos, home):
    walk_process = Walker(start_pos, home)

    while not walk_process.is_at_home():
        walk_process.move()

    return walk_process.get_steps()


if __name__ == '__main__':
    distances = [1, 2, 5, 10, 20, 50, 100]
    simulations = 5
    seed = 1

    random.seed(seed)

    for i in distances:
        path = [start_to_home(0, i)
                for j in range(simulations)
                ]
        print('Distance: {0} --> Path Lengths: {1}'.format(i, path))
