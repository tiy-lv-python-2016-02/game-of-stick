class Player:

    def __init__(self, player_input, turn=1):
        self.turn = turn
        self.player_input = player_input

    def player_input(self):
        while self.player_input:
            self.player_input = int(input("PLAYER {}: How many sticks do you take?\
            (1-3) ".format(self.turn)))
            return self.player_input


class Game:

    def __init__(self, sticks, move):
        self.sticks = int(sticks)
        self.move = move
        self.players = 2
        self.turn = 1

    def sticks_remaining(self):
        return len(range(self.sticks))

    def remove_sticks(self, removed):
        self.sticks -= int(removed)
        return self.sticks

    def __str__(self):
        return str(self.sticks) + "remain.."

    def win_condition(self):
        while self.sticks == 1 or self.sticks == 0:
            print("{} loses".format(self.turn))


if __name__ == '__main__':
    starting_sticks = input("Type the starting stick amount. 10-100:\n>>>")
    print("STARTING STICKS: {}".format(starting_sticks))
    player_move = ''
    game_start = Game(starting_sticks, player_move)


