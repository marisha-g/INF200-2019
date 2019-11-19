# -*- coding: utf-8 -*-

import random

__author__ = 'Marisha Gnanaseelan'
__email__ = 'magn@nmbu.no'


class Walker:

    def __init__(self, start, home):
        """
        :param start: initial position of the walker
        :param home: position of the walker´s home
        """
        self.x = start
        self.home = home
        self.steps = 0

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

    def is_at_home(self):
        """
        :return: true if walker is at home
        """
        return self.x == self.home

    def move(self):
        """
        :return: steps to the left(x-1) or right(x+1) with equal probability
        """
        self.x += 2 * random.randint(0, 1) - 1
        self.steps += 1


class Simulations:
    def __init__(self, start, home, seed):
        """
        Initialise the simulation

        Arguments
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        seed : int
            Random generator seed
        """
        self.start = start
        self.home = home
        random.seed(seed)

    def single_walk(self):
        """
        Simulate single walk from start to home, returning number of steps.

        Returns
        -------
        int
            The number of steps taken
        """
        walk_process = Walker(self.start, self.home)

        while not walk_process.is_at_home():
            walk_process.move()

        return walk_process.get_steps()

    def run_simulation(self, num_walks):
        """
        Run a set of walks, returns list of number of steps taken.

        Arguments
        ---------
        num_walks : int
            The number of walks to simulate

        Returns
        -------
        list[int]
            List with the number of steps per walk
        """
        return[self.single_walk() for _ in range(num_walks)]


if __name__ == '__main__':
    print(Simulations(0, 10, 12345).run_simulation(20))
    print(Simulations(0, 10, 12345).run_simulation(20))
    print(Simulations(0, 10, 54321).run_simulation(20))

    print(Simulations(10, 0, 12345).run_simulation(20))
    print(Simulations(10, 0, 12345).run_simulation(20))
    print(Simulations(10, 0, 54321).run_simulation(20))
