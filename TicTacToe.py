import random

'''
Notes: I didn't get a chance to make this code as pretty or efficient as I
would like but I was able to get the AI trained and running.

Even after 10000 games the AI plays quite badly. There is probably a much
better approach than the one I used.
'''


class Player:
    def __init__(self, number, symbol):
        self.player_number = number
        self.symbol = symbol
        self.is_human = True

    def find_moves(self, board):
        possible = []
        for i, c in enumerate(board.cells):
            if c == "_":
                possible.append(i)
        return possible

    def move(self, board):

        possible = self.find_moves(board)
        action = ""
        while not action.isnumeric() or int(action) not in possible:

            action = input(
                "Which cell to you want to move in? {}".format(possible)
            )
        return self.symbol, int(action)


class PlayerAI(Player):

    def __init__(self, number, symbol):
        super().__init__(number, symbol)
        self.is_human = False
        self.symbol = symbol
        self.hats = {}
        self.used_plays = []
        self.winning_plays = []

    def move(self, board):
        possible = self.find_moves(board)
        state = "".join(board.cells)
        if state not in self.hats:
            self.hats[state] = possible
        move = random.choice(self.hats[state])
        self.used_plays.append((state, move))
        return self.symbol, move

    def update_after_result(self, win):
        if win:
            for plays in self.used_plays:
                self.hats[plays[0]].append(plays[1])
        else:
            for plays in self.used_plays:
                if self.hats[plays[0]].count(plays[1]) > 1:
                    self.hats[plays[0]].remove(plays[1])
        self.used_plays = []

    def add_states(self, winning_hats):
        for k, v in winning_hats.items():
            if k not in self.hats:
                self.hats[k] = v

    def sim_round(self):
        """
        A single round of simulation to train the AI.
        :return: The plays of the winning player.
        """
        player2 = PlayerAI(2, "X")
        player3 = PlayerAI(3, "O")
        game = Game(player2, player3)
        winner = game.start()
        if winner == 3:
            self.winning_plays = player3.used_plays
            self.add_states(player3.hats)
        elif winner == 2:
            self.winning_plays = player2.used_plays
            self.add_states(player2.hats)
        else:
            pass  # Tie game

    def update_brain(self):
        """
        :return: Brain updated with winning plays.
        """
        for state, play in self.winning_plays:
            self.hats[state].append(play)


    def train_ai(self, rounds=10000):
        """
        Trains the brain of the AI.
        :param rounds: Number of training game.
        :return: An updated_brain.
        """
        for _ in range(rounds):
            self.sim_round()
            self.update_brain()


class Board:
    def __init__(self):
        self.cells = ["_"] * 9

    def display(self):
        print("")
        for i in range(0, 9, 3):
            print(self.cells[i:i + 3])

    def update_board(self, symbol, location):
        self.cells[location] = symbol

class Turn:
    def __init__(self, player, board):
        self.player = player
        self.board = board

    def run_turn(self):
        if self.player.is_human:
            print("It is player{}'s turn".format(self.player.player_number))
            self.board.display()
        action = self.player.move(self.board)
        self.board.update_board(action[0], action[1])
        return self.board


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.players = [player1, player2]
        self.current_player = player1
        self.board = Board()
        self.winner = None

    def switch_players(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def check_win(self):
        winning_lines = [
            "012", "345", "678", "036", "147", "258", "048", "246"
        ]
        for line in winning_lines:
            line = [int(x) for x in line]
            a = self.board.cells[line[0]]
            b = self.board.cells[line[1]]
            c = self.board.cells[line[2]]
            if a == b == c and a != "_":
                return True
        return False

    def start(self):
        while not self.winner:
            turn = Turn(self.current_player, self.board)
            self.board = turn.run_turn()
            if self.check_win():
                if self.player2.is_human:
                    print("\nPlayer{} is the winner!".format(
                        self.current_player.player_number)
                    )
                    self.board.display()
                return self.current_player.player_number
            if "_" not in self.board.cells:
                if self.player2.is_human:
                    print("It's a tie!")
                return 0
            self.switch_players()
        print("The winner is player{}!".format(self.winner))


if __name__ == '__main__':
    player1 = Player(1, "X")
    player2 = PlayerAI(2, "O")
    player2.train_ai(rounds=100000)

    game = Game(player1, player2)
    winner = game.start()
    if winner == 1:
        print("You win!")
        game.board.display()






