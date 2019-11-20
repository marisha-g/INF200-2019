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

    def test_custom_board(self):
        b = cs.Board


class TestPlayer:
    """Tests for Player
    class"""

    def test_player_has_moved(self):
        b = cs.Board()




class TestResilientPlayer:
    """Tests for Resilient
    Player class"""


class TestLazyPlayer:
    """Tests for Lazy
    Player class"""


class TestSimulation:
    """Tests for
    Simulation class"""