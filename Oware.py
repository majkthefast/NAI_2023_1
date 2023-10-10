from easyAI import TwoPlayerGame, Negamax, AI_Player, Human_Player
import numpy as np


class Oware(TwoPlayerGame):
    def __init__(self, players=None):
        self.players = players
        self.board = np.array([4] * 6 + [0] + [4] * 6)  # Początkowy stan planszy
        self.current_player = 1  # Gracz 1 rozpoczyna

    def possible_moves(self):
        if self.current_player == 1:
            return [str(i) for i in range(6) if self.board[i] != 0]
        else:
            return [str(i) for i in range(7, 13) if self.board[i] != 0]

    def make_move(self, move):
        move = int(move)
        seeds_to_sow = self.board[move]
        self.board[move] = 0
        current_position = move

        while seeds_to_sow > 0:
            current_position = (current_position + 1) % 13
            if current_position != move:
                self.board[current_position] += 1
                seeds_to_sow -= 1

    def should_collect_seeds(self, position):
        return self.board[position] in [2, 3] and 0 < position < 13 and self.current_player == 1

    def win(self):
        return sum(self.board[0:6]) - sum(self.board[7:13]) > 0

    def is_over(self):
        return not self.possible_moves()

    def scoring(self):
        return sum(self.board[0:6]) - sum(self.board[7:13])

    def show(self):
        print("Plansza:")
        print("Gracz 2 ->", self.board[7:13])
        print("           ", self.board[0:6][::-1])
        print("Gracz 1 <-")


if __name__ == "__main__":
    ai_algo = Negamax(6)  # Algorytm AI (zmień głębokość według potrzeb)
    game = Oware([AI_Player(ai_algo), Human_Player()])

    game.play()
    print("Koniec gry!")
