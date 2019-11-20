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

        :param: position
        :return: bool
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

        :param: position
        :return: self.new_position or 0
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
    """
    The Player class and its subclasses manage information about player
    position, including information on which board a player “lives”.
    """
    def __init__(self, board):
        self.board = board
        self.num_moves = 0
        self.player_position = 0
        self.roll_dice = random.randrange(1, 7, 1)

    def move(self):
        """
        The move() method moves the player by implementing a die cast,
        the following move and, if necessary, a move up a ladder or down
        a chute.

        :return: nothing
        """
        self.player_position += self.roll_dice

        event = self.board.position_adjustment(self.player_position)

        self.player_position = self.player_position + event
        self.num_moves += 1

class ResilientPlayer(Player):
    """
    This is a subclass of Player with slightly different moving behavior for
    when a player slips down a chute.
    """
    def __init__(self, board, extra_steps = 1):
        super().__init__(board)
        self.extra_steps = extra_steps

    def move(self):
        """
        When a resilient player slips down a chute, he will take extra steps
        in the next move, in addition to the roll of the dice.

        :return: self.player_position
        """
        if self.player_position in Board.chutes.values():
            self.player_position += self.extra_steps
        self.player_position += self.roll_dice
        return self.player_position

class LazyPlayer(Player):
    """
    Another subclass of Player. After climbing a ladder, a lazy player drops
    a given number of steps.
    The number of dropped steps is an optional argument to the constructor,
    default is 1.
    """
    def __init__(self, board, dropped_steps = 1):
        super().__init__(board)
        self.drop_steps = dropped_steps

    def move(self):
        """
        A lazy player never moves backward after dropping steps.

        :return: self.player_position
        """
        start_position = self.player_position

        if self.player_position in Board.ladders.values():
            self.player_position -= self.dropped_steps
            if self.player_position <= 0:
                self.player_position = start_position
        return self.player_position

class Simulation:
    def __init__(self, player_field, board, seed=123, randomize_players=False):
        self.player_field = player_field
        self.board = Board()
        self.randomize_players = randomize_players
        self.result = []
        random.seed(seed)

    def single_game(self):
        """
        Runs a single game returning a tuple consisting of the number of moves
        made and the type of the winner.
        :return:
        """
        position = [0] * self.list_of_players
        num_moves = 0

        while max(position) < self.Board.goal:
            for player in range(len(position)):
                position[player] += self.Player.roll_dice

                if position[player] in snakes_and_ladders:
                    position[player] = snakes_and_ladders[position[player]]
            num_moves += 1

        return (num_moves, self.type_of_player)

    def run_simulation(self):

        for game in range(num_games):
            self.result.append(self.single_game())

    def get_results(self):
        return self.result()

    def winners_per_type(self):
        for _ in self.type_of_player:
            winners_per_type = {self.type_of_player: num_of_wins}
        return winners_per_type

    def durations_per_type(self):
        pass

    def players_per_type(self):
        pass





