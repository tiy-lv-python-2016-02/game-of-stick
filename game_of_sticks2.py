import random

#learning my lesson and putting the new game prompt as a function outside of main

def start_new_game():
    start_game = " "
    while start_game is not "y" and start_game is not "n":
        start_game = input("Do you want to try the game again?\nType 'y' for yes. Type 'n' for no.").lower()
    return start_game == "y"

class Game:
    def __init__(self, sticks_begin, player1, player2):

        self.sticks = sticks_begin
        self.player1 = player1
        self.player2 = player2
        self.players = [self.player1, self.player2]
        self.current_player = player1

    def subtract_sticks(self, sticks_chosen):
        self.sticks -= sticks_chosen
    # unlike Game of Pig, where each player has a score, there is only one
    # score to track in this game. Therefore, I made this a method of Game
    #  rather than a method of the player class.



    def turn(self):
        for player in self.players:
            if self.player1.human_player:
                print("Player {}, it is your turn. There are {} sticks remaining on the board".format(player.player_number, self.sticks))
        pick = player.pick_sticks(self.sticks)
        self.pick_sticks(pick)

        if self.sticks == 0:
            return 0, player.player_number
        return self.sticks, 0


    def gamemplay(self):
        outcome = None
        while self.sticks > 1:
            outcome = self.turn()
            self.sticks = outcome[0]
        if self.player1.human_player:
            print("You lose, player {}.\nBetter luck next time.".format(outcome[1]))
        return outcome[1]

"""
class Hat:

    def __init__(self):

        def pick_sticks
            ...

        def losing(self)
            ...

        def winning(self)
            if self.choice == 0
                :return

            self.hat_choices.append(self.choice)

            ...

"""

class Player:

    def __init__(self, name):
        self.player_number = name
        self.human_player = True

    def pick_sticks(self, remaining_sticks):
        sticks_picked = input(int("How many sticks do you pick?"))
        if remaining_sticks > 2 and sticks_picked < 4:
            return int(pick)
        elif remaining_sticks == 2 and sticks_picked > 2:
            print ("Try again. You cannnot pick that many sticks")
        elif remaining_sticks == 1 and sticks_picked > 1:
            print ("Try again. You cannnot pick that many sticks")




    def __str__(self):
        return "I am {}".format(self.player_number)

class PlayerAI(Player):

    def __init__(self, name):
        self.name = name
        self.human_player = False


    def pick_sticks(self, sticks_remaining):
        sticks_picked = random.sticks_picked[sticks_remaining]
        print("Artificial Intelligence picks {} sticks.".format(sticks_picked))
        return sticks_picked


if __name__ == '__main__':

    print ("Let's play the Game of Sticks!\n")

    begin = " "
# Jeff will be so proud I know why I need to start with a value outside of my acceptable range here.
    while not begin.isnumeric() or int(begin) < 10 or int(begin) > 100:
        print("How many sticks are in the pile to start with?")
        begin = input("Type a number between 10 and 100.\n")

    begin = int(begin)

    game_type = " "

    while game_type != 1 and game_type != 2:
        print('You have two choices. Type "1" to play against a friend. Type "2" to play against Artificial Intelligence.')

        game_type = int(input("Please indicate which game type you want to play.\n "))

    player1 = Player(1)

    new_game = True


    if game_type == 1:
        player2 = Player(2)
    elif game_type == 2:
        player2 == PlayerAI(2)

    while new_game:
        current_game = Game(begin, player1, player2)

    if player_lost == 1 and not player2.human_player:
        player2.update_count

    new_game = start_new_game()


"""
Old Code Junkyard

#while True:
#start_game = input("Do you want to play the Game of Sticks?\n")
#if start_game.lower() != "yes":



 def start(self):

        while not self.winner:

            turn = Turn(self.current_player)
            turn_score = turn.run()

            self.current_player.record_score(turn_score)

            print("{}'s score is now {}".format(self.current_player.name,
                                                self.current_player.score))

            if self.current_player.score >= self.winning_score:
                self.winner = self.current_player
            else:
                self.switch_players()

        print("{} Wins!".format(self.current_player.name))
        return self.winner
    """

"""
    def switch_players(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1


    def remaining_sticks(self):
        x = 5
"""

"""
        while False:
            pick > 0 and pic < 4
            print("Try again!")
        else:
            return pick

    def __str__(self):
        return "I am {}".format(self.name)
"""