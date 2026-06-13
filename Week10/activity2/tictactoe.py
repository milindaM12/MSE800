from game import Game
from player import Player


class TicTacToe(Game):

    def __init__(self):
        super().__init__("Tic Tac Toe")

        self.__board = [" "] * 9

        self.player1 = Player("Player 1", "X")
        self.player2 = Player("Player 2", "O")

        self.current_player = self.player1

    def display(self):
        print("\n")
        print(f" {self.__board[0]} | {self.__board[1]} | {self.__board[2]} ")
        print("---+---+---")
        print(f" {self.__board[3]} | {self.__board[4]} | {self.__board[5]} ")
        print("---+---+---")
        print(f" {self.__board[6]} | {self.__board[7]} | {self.__board[8]} ")
        print()

    def make_move(self, position):

        if self.__board[position] == " ":
            self.__board[position] = self.current_player.get_symbol()
            return True

        return False

    def check_winner(self):

        winning_positions = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ]

        for combo in winning_positions:

            if (
                self.__board[combo[0]]
                == self.__board[combo[1]]
                == self.__board[combo[2]]
                != " "
            ):
                return True

        return False

    def is_draw(self):
        return " " not in self.__board

    def switch_player(self):

        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def play(self):

        while True:

            self.display()

            try:
                position = int(
                    input(
                        f"{self.current_player.get_name()} "
                        f"({self.current_player.get_symbol()}) "
                        f"Enter position (1-9): "
                    )
                ) - 1

                if position < 0 or position > 8:
                    print("Invalid position.")
                    continue

                if not self.make_move(position):
                    print("Position already occupied.")
                    continue

                if self.check_winner():
                    self.display()

                    print(
                        f"{self.current_player.get_name()} wins!"
                    )
                    break

                if self.is_draw():
                    self.display()
                    print("Game Draw!")
                    break

                self.switch_player()

            except ValueError:
                print("Enter a valid number.")