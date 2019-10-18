# -*- coding: utf-8 -*-

import random
import statistics

__author__ = 'Marisha Gnanaseelan', 'Peter Langdalen'
__email__ = 'magn@nmbu.no', 'pelangda@nmbu.no'


snakes_and_ladders = {1:40,
                      8:10,
                      36:52,
                      43:62,
                      49:79,
                      65:82,
                      68:85,
                      24:5,
                      33:3,
                      42:30,
                      56:37,
                      64:27,
                      74:12,
                      87:70
                      }

def single_game(num_players):
    """
    Returns duration of single game.

    Arguments
    ---------
    num_players : int
        Number of players in the game

    Returns
    -------
    num_moves : int
        Number of moves the winning player needed to reach the goal
    """
    position = [0] * num_players
    num_moves = 0

    while max(position) < 90:
        for player in range(len(position)):
            roll = random.randint(1, 6)
            position[player] += roll

            if position[player] in snakes_and_ladders:
                position[player] = snakes_and_ladders[position[player]]
            num_moves += 1

        return num_moves


def multiple_games(num_games, num_players):
    """
    Returns durations of a number of games.

    Arguments
    ---------
    num_games : int
        Number of games to play
    num_players : int
        Number of players in the game

    Returns
    -------
    num_moves : list
        List with the numbedr of moves needed in each game.
    """
    num_moves = [0] * num_games

    for games in range(num_games):
        num_moves[games] = single_game(num_players)
    return num_moves


def multi_game_experiment(num_games, num_players, seed):
    """
    Returns durations of a number of games when playing with given seed.

    Arguments
    ---------
    num_games : int
        Number of games to play
    num_players : int
        Number of players in the game
    seed : int
        Seed used to initialise the random number generator

    Returns
    -------
    num_moves : list
        List with the numbedr of moves needed in each game.
    """


if __name__ == '__main__':
    multi_game_experiment()
