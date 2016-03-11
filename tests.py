from unittest import TestCase
from sticks import Hat, HatAIPlayer, Game


class HatAIPlayerTests(TestCase):

    def setUp(self):

        self.player = HatAiPlayer("Tester")

    def test_init(self):

        self.assertEqual(self.player.name, "Tester", msg="Name incorrect")
        self.assertEqual(self.player.win, 0, msg="Win not starting at 0")
        self.assertEqual(self.player.loss, 0, msg="Loss not starting at 0")
        self.assertEqual(self.player.hats, [], msg="Hats not reset for session")

    def test_take_sticks(self):

        take_sticks = self.player.take_sticks()
        self.assertTrue(1 <= take_sticks <= 3, msg="Not taking sticks")


class GameTests(TestCase):

    def setUp(self):

        self.player1 = Player("Player 1")
        self.player2 = Player("Player 2")

    def test_init(self):

        self.assertEqual(self.player1.name, "Player 1", msg="P1 name incorrect")
        self.assertEqual(self.player2.name, "Player 2", msg="P2 name incorrect")


