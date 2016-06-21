from unittest import TestCase
from sticks import HatAIPlayer, Game, Player


class HatAIPlayerTests(TestCase):

    def setUp(self):
        self.sticks = 10
        self.player = HatAIPlayer("Tester", self.sticks)

    def test_init(self):

        self.assertEqual(self.player.name, "Tester", msg="Name incorrect")
        self.assertEqual(self.player.win, 0, msg="Win not starting at 0")
        self.assertEqual(self.player.loss, 0, msg="Loss not starting at 0")


class GameTests(TestCase):

    def setUp(self):

        sticks = 10
        self.player1 = Player("Player 1")
        self.player2 = Player("Player 2")
        self.test_game = Game(self.player1, self.player2, sticks)

    def test_init(self):

        self.assertEqual(self.player1.name, "Player 1", msg="P1 name incorrect")
        self.assertEqual(self.player2.name, "Player 2", msg="P2 name incorrect")


