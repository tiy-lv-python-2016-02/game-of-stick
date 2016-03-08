class Game:

    def __init__(self, beginning_sticks, player1, player2):
        self.beginning_sticks = beginning_sticks
        self.player1 = player1
        self.player2 = player2
        self.players = [self.player1, self.player2]


    def whose_turn(self):
        # This is how we switch from player 1 to player 2
        for player in self.player:
            print("{}, it is your turn".format(player.player_number))
            print("There are {} sticks on the table.".format(self.remaining_sticks))
            # come back to this


    def execute_game(self):
        while remaining_sticks > 0:
            play = self.whose_turn()


class Player:
    def __init__(self, player_number):
        self.player_number = player_number

    def make_choice(self, sticks_removed, remaining_sticks):
        sticks_removed = input("How many sticks do you choose?")
        if sticks_removed > 3:
            print("Please choose a number between 1 and 3")
        elif sticks_removed > int(remaining_sticks):
            print("There are not that many sticks left on the table.")
        else:
             print("x") # this is a placeholder

if __name__ == '__main__':

    player1 = Player(1)
    player2 = Player(2)

    print("Let's play the Game of Sticks!\n")

    # This is how we determine the number of sticks in the starting pile
    beginning_sticks = int(input("How many sticks are on the table? Choose a number between 10 and 50. \n"))

    while beginning_sticks < 10 or beginning_sticks > 50:
        print("Try again. Please choose a number between 10 and 50.")
    else:
        gameplay = Game(beginning_sticks, player1, player2)







# while True:
# start_game = input("Do you want to play the Game of Sticks?\n")
# if start_game.lower() != "yes":
# break