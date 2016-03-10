import random


def next_game():
    """
    Prompts user to ask if they want to play another game.
    :return: Player input.
    """
    print("")
    another_game = " "
    while another_game not in "yn":
        another_game = input("Play again? [y/n]: ").lower()
    return another_game == "y"


class Player:
    """
    Player class that makes decisions on how many sticks to pick up.
    """
    def __init__(self, number):
        self.player_number = number
        self.is_human = True

    def make_selection(self, total_sticks):
        """
        Requires player to make a valid selection.
        :param total_sticks: Total remaining sticks.
        :return: Player choice of how many sticks to remove.
        """
        choice = " "
        most = min([3, int(total_sticks)])
        while not choice.isnumeric() or int(choice) > most:
            choices = [str(x) for x in range(1, most+1)]
            choices = " or ".join(choices)
            print("How many sticks would you like to take?")
            choice = input("{}: ".format(choices))
        return int(choice)

    def __str__(self):
        return "I am player number {}".format(self.player_number)


class PlayerAI(Player):
    """
    Player class that is run by a learning AI.
    """
    def __init__(self, number, max_starting=100):
        super().__init__(number)
        self.used_plays = []
        self.is_human = False
        self.max_starting = max_starting
        self.winning_plays = []

        hats = {i: [1, 2, 3] for i in range(3, self.max_starting + 1)}
        hats[2] = [1, 2]
        hats[1] = [1]
        self.hats = hats

    def sim_round(self):
        """
        A single round of simulation to train the AI.
        :return: The plays of the winning player.
        """
        player3 = PlayerAI(3)
        player2 = PlayerAI(2)
        game = Game(self.max_starting, player2, player3)
        loser = game.run_game()
        if loser == 2:
            self.winning_plays = player3.used_plays
        else:
            self.winning_plays = player2.used_plays

    def update_brain(self):
        """
        :return: Brain updated with winning plays.
        """
        for sticks, play in self.winning_plays:
            self.hats[sticks].append(play)

    def train_ai(self, rounds=10000):
        """
        Trains the brain of the AI.
        :param rounds: Number of training game.
        :return: An updated_brain.
        """
        for _ in range(rounds):
            self.sim_round()
            self.update_brain()

    def make_selection(self, total_sticks):
        """
        AI player randomly selects a choice.
        :param total_sticks: The current number of sticks for current play.
        :return: Number of sticks to pick up.
        """
        choice = random.choice(self.hats[total_sticks])
        if self.is_human:
            print("The AI selects {}".format(choice))
        self.used_plays.append((total_sticks, choice))
        return choice

    def update_after_result(self, win):
        """
        Updates the play dictionary after a game finishes.
        :param win: Whether or not the AI won the last game.
        :return: A new hats dictionary and clean used_plays list.
        """
        if win:
            for plays in self.used_plays:
                self.hats[plays[0]].append(plays[1])
        else:
            for plays in self.used_plays:
                if self.hats[plays[0]].count(plays[1]) > 1:
                    self.hats[plays[0]].remove(plays[1])
        self.used_plays = []


class Game:
    """
    This is the main game class which takes two players as arguments,
    handles the turns, and declares a winner.

    The print statements are put under if statements so that they do not
    run when there is no human player in the game. This is very nice
    when training two AI players against each other.
    """
    def __init__(self, starting_sticks, player1, player2):
        self.sticks = starting_sticks
        self.player1 = player1
        self.player2 = player2
        self.players = [self.player1, self.player2]

    def remove_sticks(self, number):
        """
        Remove sticks from self.sticks.
        """
        self.sticks -= number

    def turn(self):
        """
        One turn of gameplay. Both players act and the number of sticks is
        adjusted appropriately.
        :return: A tuple of the remaining sticks and either the losing
        player number or zero.
        """
        for player in self.players:
            if self.player1.is_human:
                print("\nIt is player {}'s turn".format(player.player_number))
                print("There are {} sticks on the board".format(self.sticks))
            action = player.make_selection(self.sticks)
            self.remove_sticks(action)

            if self.sticks < 1:
                return 0, player.player_number
        return self.sticks, 0

    def run_game(self):
        """
        The main game function.
        :return: Player number of losing the losing player.
        """
        results = None
        while self.sticks > 0:
            results = self.turn()
            self.sticks = results[0]
        if self.player1.is_human:
            print("Player {} has lost.".format(results[1]))
            print("Game over")
        return results[1]


if __name__ == '__main__':

    print("Welcome to Game of Sticks!")
    starting = " "

    while not starting.isnumeric() or int(starting) not in range(10, 101):
        print("How many sticks are you putting on the board?")
        starting = input("Please enter a number 10-100: ")

    starting = int(starting)

    game_mode = " "

    while not game_mode.isnumeric() or int(game_mode) not in [1, 2, 3]:
        print("Options:",
              "Play against a friend (1)",
              "Play against the computer (2)",
              "Play against a trained AI (3)",
              sep="\n"
              )

        game_mode = input("Please select an option... ")

    game_mode = int(game_mode)
    new_game = True

    player1 = Player(1)

    if game_mode == 1:
        player2 = Player(2)
    elif game_mode == 2:
        player2 = PlayerAI(2)
    elif game_mode == 3:
        print("Training AI...")
        player2 = PlayerAI(2)
        player2.train_ai()
        print(player2.hats[8][:12])

    while new_game:
        active_game = Game(starting, player1, player2)
        loser = active_game.run_game()

        # Update hats if player2 is an AI.
        if loser == 1 and not player2.is_human:
            player2.update_after_result(True)
        elif loser == 2 and not player2.is_human:
            player2.update_after_result(False)

        new_game = next_game()


"""
Strategy analysis.

The optimal strategy for Game of Sticks can be found by working backwards
from the end. A player can always win if they have 2, 3, or 4 sticks at
the start of their turn since they will be able to leave their opponent with
exactly one.

The only way to force an opponent to leave 2, 3, 4 sticks is to start their
turn with 5. In other words, if your opponent starts a turn with 5 sticks
remaining, you can always win.

Given that leaving the other player with 5 sticks is a guaranteed win,
starting a turn with 6, 7, or 8 sticks is likewise a win. The only
way to start a turn with 6, 7, or 8 sticks? Have your opponent start their
turn with exactly 9.

The strategy ends up being fairly simple. If you can force your opponent to
start their turn with 5 sticks in play or 9, 13, 17, or any multiple of 4
after that, you can always win.
"""
