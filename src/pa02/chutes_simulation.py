# -*- coding: utf-8 -*-

import random

__author__ = 'Marisha Gnanaseelan', 'Peter Langdalen'
__email__ = 'magn@nmbu.no', 'pelangda@nmbu.no'


class Board:
    """
    The Board class shall manage all information about ladders, snakes,
    and the goal.
    """

    ladders = {
        1: 40,
        8: 10,
        36: 52,
        43: 62,
        49: 79,
        65: 82,
        68: 85
    }

    chutes = {
        24: 5,
        33: 3,
        42: 30,
        56: 37,
        64: 27,
        74: 12,
        87: 70
    }

    goal = 90

    def __init__(self, ladders = None, chutes = None, goal = None):
        if ladders is None:
            self.ladders = Board.ladders
        if chutes is None:
            self.chutes = Board.chutes
        if goal is None:
            self.goal = Board.goal

        self.new_position = 0

    def goal_reached(self, position):
        """
        Returns true if it is passed a position at or beyond the goal
        :param position:
        :return:
        """

        if position >= self.goal:
            return True
        else:
            return False

    def position_adjustment(self, position):
        """
        Handles changes in position due to snakes and ladders.
        It accepts a position as argument and returns the number of positions
        the player must move forward (in case of a ladder) or backward (chute),
        to get to the correct position. If the player is not at the start of a
        chute or ladder, the method returns 0.
        :param position:
        :return:
        """
        if position in self.ladders.keys():
            self.new_position = self.ladders[position] - position
            return self.new_position
        elif position in self.chutes.keys():
            self.new_position = position - self.ladders[position]
            return - self.new_position
        else:
            return 0

class Player:
    def __init__(self, board):
        self.board = board
        self.num_moves = 0
        self.player_position = 0
        self.roll_dice = random.randrange(1, 7, 1)

    def move(self):
        self.player_position += self.roll_dice

        event = self.board.position_adjustment(self.player_position)

        self.player_position = self.player_position + event
        self.num_moves += 1

class ResilientPlayer(Player):
    def __init__(self, board, extra_steps = 1):
        super().__init__(board)
        self.extra_steps = extra_steps

    def move(self):
        if self.player_position in Board.chutes.values():
            self.player_position += self.extra_steps
        self.player_position += self.roll_dice
        return self.player_position