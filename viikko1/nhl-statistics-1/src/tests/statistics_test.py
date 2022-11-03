import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(PlayerReaderStub())

    def test_search_works(self):
        player = self.statistics.search("Semenko")
        semenko = Player("Semenko", "EDM", 4, 12)
        self.assertEqual(player.__str__(), semenko.__str__())

        empty_player = self.statistics.search("Matti")
        self.assertEqual(empty_player, None)

    def test_team_works(self):
        team = self.statistics.team("PIT")
        PIT = [
            self.statistics.search("Lemieux")
        ]
        self.assertEqual(team, PIT)

    def test_top_works(self):
        sorted_players = self.statistics.top(0)
        players = [
            self.statistics.search("Gretzky"),
            #self.statistics.search("Yzerman"),
        ]
        self.assertEqual(sorted_players, players)



