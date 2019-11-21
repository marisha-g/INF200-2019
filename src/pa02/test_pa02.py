# -*- coding: utf-8 -*-

__author__ = 'Marisha Gnanaseelan', 'Peter Langdalen'
__email__ = 'magn@nmbu.no', 'pelangda@nmbu.no'

import chutes_simulation as cs


class TestPa02Board:
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

    def test_position_adjusment(self):
        b = cs.Board()
        pos = b.position_adjustment(1)
        assert pos == 39


class TestPa02Player:
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


class TestPa02ResilientPlayer:
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


class TestPa02LazyPlayer:
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


class TestPa02Simulation:

    def test_single_game(self):
        s = cs.Simulation([cs.Player, cs.Player])
        end = s.single_game()
        assert type(end) == tuple

    def test_winners_per_type(self):
        s = cs.Simulation([cs.Player])
        s.run_simulation(6)
        w = s.winners_per_type()
        assert w['Player'] == 6

    def test_durations_per_type(self):
        s = cs.Simulation([cs.LazyPlayer, cs.Player])
        s.run_simulation(10)
        w = s.durations_per_type()
        assert w['Player'] or w['LazyPlayer'] == int

    def test_players_per_type(self):
        s = cs.Simulation([cs.Player, cs.LazyPlayer, cs.ResilientPlayer])
        s.run_simulation(10)
        w = s.durations_per_type()
        assert type(w['Player']) == list