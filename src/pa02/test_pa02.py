# -*- coding: utf-8 -*-

__author__ = 'Marisha Gnanaseelan', 'Peter Langdalen'
__email__ = 'magn@nmbu.no', 'pelangda@nmbu.no'

import chutes_simulation as cs


class TestBoard:
    """Tests for Board
    class"""

    def test_default_board(self):
        b = cs.Board()

        assert b.ladders == {1: 40, 8: 10, 36: 52, 43: 62,
                             49: 79, 65: 82, 68: 85}
        assert b.chutes == {24: 5, 33: 3, 42: 30, 56: 37,
                            64: 27, 74: 12, 87: 70}
        assert b.goal == 90

    def test_goal_reached(self):
        b = cs.Board()
        goal = b.goal_reached(90)
        assert goal is True


class TestPlayer:
    """Tests for Player
    class"""

    def test_move_player(self):
        b = cs.Board()
        p = cs.Player(b)
        p.move()

        assert p.player_position > 0
        assert p.player_position not in b.chutes.keys() and b.ladders.keys()

        position1 = p.player_position
        p.move()
        assert p.player_position != position1


class TestResilientPlayer:
    """Tests for Resilient
    Player class"""
    def test_move_resilientplayer(self):
        b = cs.Board()
        p = cs.ResilientPlayer(b)
        p.move()

        assert p.player_position > 0
        assert p.player_position not in b.chutes.keys() and b.ladders.keys()

        position1 = p.player_position
        p.move()
        assert p.player_position != position1


class TestLazyPlayer:
    """Tests for Lazy
    Player class"""
    def test_move_lazyplayer(self):
        b = cs.Board()
        p = cs.LazyPlayer(b)
        p.move()

        assert p.player_position > 0
        assert p.player_position not in b.chutes.keys() and b.ladders.keys()

        position1 = p.player_position
        p.move()
        assert p.player_position != position1


class TestSimulation:
    """Tests for
    Simulation class"""



