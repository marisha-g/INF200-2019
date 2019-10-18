# -*- coding: utf-8 -*-

__author__ = 'Marisha Gnanaseelan', 'Peter Langdalen'
__email__ = 'magn@nmbu.no', 'pelangda@nmbu.no'


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
    num_players = input(int('How many players? '))
    position = 0
    num_moves = 0

    if num_players < 1:
        print('Has to be one or more.')


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
