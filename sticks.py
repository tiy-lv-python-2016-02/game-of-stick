import random


class Player:

    def __init__(self, name):
        self.name = name

    def take_sticks(self, total_sticks):
        """
        Takes user input on how many sticks they want to pick up.
        :param total_sticks: Current total sticks
        :return: Player's answer to how many sticks they want to remove.
        """
        answer = ""
        while not answer.isnumeric() or int(answer) not in range(1,4):
            answer = input("{}: How many sticks do you take? (1-3) "\
                           .format(self.name))
        return answer


class DumbAIPlayer(Player):
    """
    AI player that always takes 3 sticks when the amount is greater
    than 4. If less than 4, it'll pick up just enough to leave the
    other player with 1.
    """

    def take_sticks(self, total_sticks):

        if total_sticks >= 4:
            answer = 3
        elif total_sticks <= 4:
            answer = total_sticks - 1
        print("Dumb AI Player took {} stick(s).".format(answer))
        return answer


class HatAIPlayer(Player):

    def __init__(self, name):
        super().__init__(name)
        pass


class RandomAI(Player):
    """
    Picks up a random number of sticks every turn
    """

    def take_sticks(self, total_sticks):
        answer = random.randint(1, 3)
        print("Random AI Player took {} stick(s).".format(answer))
        return answer


class Game:

    def __init__(self, player1, player2, starting_sticks):
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.sticks = starting_sticks
        self.loser = None

    def start(self):

        while self.sticks >= 2:
            print("{} sticks remain.".format(self.sticks))
            self.sticks -= int(self.current_player.take_sticks(self.sticks))
            self.switch_player()

        print("{} had to pick up the last stick. {} Loses.".format
              (self.current_player.name, self.current_player.name))

    def switch_player(self):

        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

if __name__ == '__main__':

    print("How many sticks would you like to start?")

    mode = ""

    sticks_to_start = ""

    while not sticks_to_start.isnumeric() or int(sticks_to_start)\
            not in range(10, 101):
        sticks_to_start = input("Enter a number 10-100: ")

    sticks_to_start = int(sticks_to_start)

    print("\nPlay against a (1)friend or play against the (2)computer?")

    while not mode.isnumeric() or int(mode) not in [1, 2]:
        mode = input("\n~>")

    mode = int(mode)

    if mode == 1:
        player1 = Player("Player 1")
        player2 = Player("Player 2")
    else:
        player1 = Player("Player 1")
        player2 = DumbAIPlayer("Player 2")

    game = Game(player1, player2, sticks_to_start)

    while 100 >= sticks_to_start >= 10:
        game.start()
        break
