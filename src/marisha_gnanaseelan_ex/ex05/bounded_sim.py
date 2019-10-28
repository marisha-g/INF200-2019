# -*- coding: utf-8 -*-

from walker_sim import Walker, Simulation
import random

__author__ = 'Marisha Gnanaseelan'
__email__ = 'magn@nmbu.no'


class BoundedWalker(Walker):
    def __init__(self, start, home, left_limit, right_limit):
        """
        Initialise the walker

        Arguments
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        left_limit : int
            The left boundary of walker movement
        right_limit : int
            The right boundary  of walker movement
        """
        self.x = start
        self.home = home
        self.left = left_limit
        self.right = right_limit

        super().__init__(self.x, self.home)

    def move(self):
        """

        :return:
        """
        super().move()

        if self.x < self.left:
            self.x = self.left
        elif self.x > self.right:
            self.x = self.right


class BoundedSimulation:
    def __init__(self, start, home, seed, left_limit, right_limit):
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
        left_limit : int
            The left boundary of walker movement
        right_limit : int
            The right boundary  of walker movement
        """
        self.x = start
        self.home = home
        self.left = left_limit
        self.right = right_limit
        _seed = random.seed(seed)

        super().__init__(self.x, self.home, _seed)

    def single_walk(self):
        """
        Simulate single walk from start to home, returning number of steps.
        :return: int
                The number of steps taken
        """
        walk_process = BoundedWalker(self.start, self.home,
                                     self.left, self.right)

        num_steps = 0
        while not walk_process.is_at_home():
            walk_process.move()
            num_steps += 1
        return num_steps


if __name__ == '__main__':

    for left_boundaries in [0, -10, -100, -1000, -1000]:

