import random


def next_game():
    """
    Prompts user to ask if they want to play another game.
    :return: Player input.
    """
    print("")
    next_game = " "
    while next_game not in "yn":
        next_game = input("Play again? [y/n]: ").lower()
    return next_game == "y"


class Player:
    """
    Player class that makes decisions on how many sticks to pick up.
    """

    def __init__(self, number):
        self.player_number = number

    def make_selection(self, total_sticks):
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
    def __init__(self, number):
        super().__init__(number)
        self.used_plays = []

    def initialize_hat(self, max_number=100):
        # Run on initial setup
        self.hats = {i: [1,2,3] for i in range(3, max_number + 1)}
        self.hats[2] = [1, 2]
        self.hats[1] = [1]
        return self.hats

    def make_selection(self, total_sticks):
        choice = random.choice(self.hats[total_sticks])
        print("The AI selects {}".format(choice))
        self.used_plays.append((total_sticks, choice))
        return choice

    def update_after_result(self, win):
        if win:
            for plays in self.used_plays:
                self.hats[plays[0]].append(plays[1])
        else:
            for plays in self.used_plays:
                if len(self.hats[plays[0]]) > 1:
                    self.hats[plays[0]].remove(plays[1])
        self.used_plays = []


class Game:
    def __init__(self, starting_sticks, player1, player2):
        self.sticks = starting_sticks
        self.player1 = player1
        self.player2 = player2
        self.players = [self.player1, self.player2]

    def turn(self):

        for player in self.players:
            print("\nIt is player {}'s turn".format(player.player_number))
            print("There are {} sticks on the board".format(self.sticks))
            action = player.make_selection(self.sticks)
            self.sticks -= action

            if self.sticks < 1:
                #print("Player {} has lost".format(player.player_number))
                return 0, player.player_number
        return self.sticks, 0  # Better way?

    def run_game(self):
        while self.sticks > 0:
            results = self.turn()
            self.sticks = results[0]
        print("Player {} has lost.".format(results[1]))
        print("Game over")
        return results[1]


# Options to play against computer or human
# Option to play again
# - must preserve AI brain

if __name__ == '__main__':

    print("Welcome to Game of Sticks!")
    starting = " "

    while not starting.isnumeric() or int(starting) not in range(10, 101):
        print("How many sticks are you putting on the board?")
        starting = input("Please enter a number 10-100: ")

    starting = int(starting)

    game_mode = '0'

    while not game_mode.isnumeric() or int(game_mode) not in [1, 2]:
        print("Options:",
              "Play against a friend (1)",
              "Play against the computer (2)",
              sep="\n"
              )

        game_mode = input("Please select an option... ")

    game_mode = int(game_mode)
    new_game = True

    if game_mode == 1:
        player1 = Player(1)
        player2 = Player(2)

        while new_game:
            active_game = Game(starting, player1, player2)
            active_game.run_game()
            new_game = next_game()

    elif game_mode == 2:
        player1 = Player(1)
        player2 = PlayerAI(2)
        player2.initialize_hat(max_number=10)

        while new_game:
            active_game = Game(starting, player1, player2)
            loser = active_game.run_game()
            if loser == 1:
                player2.update_after_result(True)
            else:
                player2.update_after_result(False)
            print(player2.hats)

            new_game = next_game()



