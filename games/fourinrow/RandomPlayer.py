from random import randint
from Player import Player

class RandomPlayer(Player):

    def name(self):
        return "Random"

    def move(self, player_code, board):
        return randint(0, 6)


