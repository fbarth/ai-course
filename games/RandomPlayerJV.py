from random import randint
from Player import Player

class RandomPlayerJV(Player):

    def name(self):
        return "Random JV"

    def move(self, player_code, board):
        x = 0
        while True:
            x = randint(0, 8)
            if board[x] == 0:
                break
        return x


