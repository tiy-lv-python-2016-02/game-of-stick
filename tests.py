from GameOfSticks import PlayerAI, Game
from unittest import TestCase


class PlayerAITests(TestCase):

    def setUp(self):
        self.player = PlayerAI(2)

    def test_init(self):
        self.assertFalse(self.player.is_human)
        self.assertEqual(self.player.max_starting, len(self.player.hats))

    def test_make_selection(self):
        self.assertTrue(self.player.make_selection(10) in [1, 2, 3])

    def test_update_after_result(self):

        self.player.used_plays = [(8, 3)]
        self.player.update_after_result(True)
        new_play = self.player.hats[8]
        self.assertTrue(
            new_play == [1, 2, 3, 3], msg="Plays: {}".format(new_play)
        )


class RiggedAI(PlayerAI):

    def make_selection(self, total_sticks):
        return 1


class GameTests(TestCase):

    def setUp(self):
        self.player1 = PlayerAI(1)
        self.player2 = PlayerAI(2)
        self.game = Game(100, self.player1, self.player2)

    def test_init(self):
        self.assertEqual(
            self.game.players, [self.game.player1, self.game.player2]
        )

    def test_remove_sticks(self):
        self.game.remove_sticks(25)
        self.assertEqual(self.game.sticks, 75)

    def test_run_game(self):

        self.player1 = RiggedAI(1)
        self.player2 = RiggedAI(2)
        self.game = Game(100, self.player1, self.player2)

        loser = self.game.run_game()

        self.assertTrue(loser == 2, msg="Winner {}".format(loser))
