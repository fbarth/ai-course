from Player import Player

class ManualPlayerJV(Player):

    def name(self):
        return "Manual"

    def move(self, player_code, board):
        g = input("Enter a position (0..8) : ") 
        return int(g)
