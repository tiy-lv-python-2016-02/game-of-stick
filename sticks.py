import random


class Player:

    def __init__(self, name):
        self.name = name
        self.win = 0
        self.loss = 0

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

    def winning(self):
        self.win += 1

    def losing(self):
        self.loss += 1


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


class Hat:

    def __init__(self):
        self.hat_choices = [1, 2, 3]
        self.choice = 0

    def pick_sticks(self):

        self.choice = random.choice(self.hat_choices)
        return self.choice

    def losing(self):
        if self.choice == 0:
            return

        if self.hat_choices.count(self.choice) > 1:
            index = self.hat_choices.index(self.choice)
            del self.hat_choices[index]

        self.choice = 0

    def winning(self):
        if self.choice == 0:
            return

        self.hat_choices.append(self.choice)

        self.choice = 0


class HatAIPlayer(Player):

    def __init__(self, name, sticks_to_start):
        super(HatAIPlayer, self).__init__(name)
        self.name = name
        self.hats = []

        for stick in range(1, sticks_to_start + 1):
            self.hats.append(Hat())

    def take_sticks(self, remaining_sticks):

        sticks_taken = self.hats[remaining_sticks].pick_sticks()
        print("AI player took {} sticks.".format(sticks_taken))
        return sticks_taken

    def winning(self):

        for hat in self.hats:
            hat.winning()

    def losing(self):

        for hat in self.hats:
            hat.losing()


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

    def start(self):

        while self.sticks >= 2:
            print("{} sticks remain.".format(self.sticks))
            self.sticks -= int(self.current_player.take_sticks(self.sticks))
            self.switch_player()

        print("{} had to pick up the last stick. {} Loses.".format
              (self.current_player.name, self.current_player.name))

        if self.current_player == self.player2:
            self.player2.losing()
            self.player1.winning()
        else:
            self.player2.winning()
            self.player1.losing()

    def switch_player(self):

        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1


if __name__ == '__main__':

    mode = ""

    sticks_to_start = ""

    print("How many sticks would you like to start?")

    while not sticks_to_start.isnumeric() or int(sticks_to_start)\
            not in range(10, 101):
        sticks_to_start = input("Enter number 10-100: ")

    sticks_remain = int(sticks_to_start)

    print("\n(1)Train AI\n(2)AI training against the computer?")

    while not mode.isnumeric() or int(mode) not in [1, 2]:
        mode = input("\n~>")

    mode = int(mode)

    play = True

    if mode == 1:
        player1 = Player("Player 1")
        player2 = HatAIPlayer("Player 2", sticks_remain)
    else:
        player1 = DumbAIPlayer("Player 1")
        player2 = HatAIPlayer("Player 2", sticks_remain)

    while play:

        first_game = Game(player1, player2, sticks_remain)
        first_game.start()

        play_again = input("Play again? y/n? ")

        if play_again == "y":
            play = True
            sticks_remain = int(sticks_to_start)
        else:
            play = False
