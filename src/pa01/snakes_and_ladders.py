# -*- coding: utf-8 -*-

import random
import statistics

__author__ = 'Marisha Gnanaseelan', 'Peter Langdalen'
__email__ = 'magn@nmbu.no', 'pelangda@nmbu.no'


snakes_and_ladders = {1: 40,
                      8: 10,
                      36: 52,
                      43: 62,
                      49: 79,
                      65: 82,
                      68: 85,
                      24: 5,
                      33: 3,
                      42: 30,
                      56: 37,
                      64: 27,
                      74: 12,
                      87: 70
                      }


def single_game(num_players):
    """
    Returns duration of single game.

    Source:
    https://jakevdp.github.io/blog/2017/12/18/simulating-chutes-and-ladders/

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

    for game in range(num_games):
        num_moves[game] = single_game(num_players)

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
    random.seed(seed)
    return multiple_games(num_games, num_players)


if __name__ == '__main__':
    number_of_players = 4
    number_of_games = 100
    random_seed = 1

    number_of_moves = multi_game_experiment(number_of_players,
                                            number_of_games, random_seed)

    print(f' The shortest game duration is {(min(number_of_moves))} and '
          f'the longest game duration is {(max(number_of_moves))}.')

    print(f' The median game duration is {statistics.median(number_of_moves)}')

    print(f' The mean game duration is {statistics.mean(number_of_moves)} and '
          f'the standard deviation is {statistics.stdev(number_of_moves)}')

