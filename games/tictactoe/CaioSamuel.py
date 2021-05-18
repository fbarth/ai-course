from Player import Player
import numpy as np

#
# Authors: Caio e Samuel
#

class CaioSamuel(Player):

    def name(self):
        return 'Caio e Samuel'

    def temVencedor(self, tabuleiro):
        if((tabuleiro[0] == tabuleiro[1] == tabuleiro[2]) & (tabuleiro[0] != 0)):
            return True
        elif((tabuleiro[3] == tabuleiro[4] == tabuleiro[5]) & (tabuleiro[3] != 0)):
            return True
        elif((tabuleiro[6] == tabuleiro[7] == tabuleiro[8]) & (tabuleiro[6] != 0)):
            return True
        elif((tabuleiro[0] == tabuleiro[3] == tabuleiro[6]) & (tabuleiro[0] != 0)):
            return True
        elif((tabuleiro[1] == tabuleiro[4] == tabuleiro[7]) & (tabuleiro[1] != 0)):
            return True
        elif((tabuleiro[2] == tabuleiro[5] == tabuleiro[8]) & (tabuleiro[2] != 0)):
            return True
        elif((tabuleiro[0] == tabuleiro[4] == tabuleiro[8]) & (tabuleiro[0] != 0)):
            return True
        elif((tabuleiro[2] == tabuleiro[4] == tabuleiro[6]) & (tabuleiro[2] != 0)):
            return True
        else:
            return False

    def vencedor(self, tabuleiro, player):
        if tabuleiro[0] == tabuleiro[1] and tabuleiro[0] == tabuleiro[2] and tabuleiro[0] == player:
            return True
        elif (tabuleiro[3] == tabuleiro[4] and tabuleiro[3] == tabuleiro[5] and tabuleiro[3] == player):
            return True
        elif (tabuleiro[6] == tabuleiro[7] and tabuleiro[6] == tabuleiro[8] and tabuleiro[6] == player):
            return True
        elif (tabuleiro[0] == tabuleiro[3] and tabuleiro[0] == tabuleiro[6] and tabuleiro[0] == player):
            return True
        elif (tabuleiro[1] == tabuleiro[4] and tabuleiro[1] == tabuleiro[7] and tabuleiro[1] == player):
            return True
        elif (tabuleiro[2] == tabuleiro[5] and tabuleiro[2] == tabuleiro[8] and tabuleiro[2] == player):
            return True
        elif (tabuleiro[0] == tabuleiro[4] and tabuleiro[0] == tabuleiro[8] and tabuleiro[0] == player):
            return True
        elif (tabuleiro[6] == tabuleiro[4] and tabuleiro[6] == tabuleiro[2] and tabuleiro[6] == player):
            return True
        else:
            return False

    def checkForDraw(self, tabuleiro):
        for i in range(0,9):
            if tabuleiro[i] == 0:
                return False
        if self.temVencedor(tabuleiro):
            return False
        else:
            return True

    def opponent(self, player_code):
        if player_code == 1:
            return 2
        if player_code == 2:
            return 1

    def minimax(self, tabuleiro, isMax, player_code):
        if self.vencedor(tabuleiro, player_code):
            return 100
        elif self.vencedor(tabuleiro, self.opponent(player_code)):
            return -100
        elif self.checkForDraw(tabuleiro):
            return 0

        if isMax:
            bestScore = -1000

            for i in range(0,9):
                if(tabuleiro[i] == 0):
                    tabuleiro[i] = player_code
                    score = self.minimax(tabuleiro, False, player_code)
                    tabuleiro[i] = 0
                    if (score > bestScore):
                        bestScore = score
            return int(bestScore)

        else:
            bestScore = 1000

            for i in range(0,9):
                if(tabuleiro[i] == 0):
                    tabuleiro[i] = self.opponent(player_code)
                    score = self.minimax(tabuleiro,True, player_code)
                    tabuleiro[i] = 0
                    if (score < bestScore):
                        bestScore = score
            return int(bestScore)

    def move(self, player_code, tabuleiro):
        bestScore = -1000
        bestMove = 0

        for i in range(0, 9):
            if(tabuleiro[int(i)] == 0):
                tabuleiro[int(i)] = player_code
                score = self.minimax(tabuleiro,False,player_code)
                tabuleiro[i] = 0
                if (score > bestScore):
                    bestScore = score
                    bestMove = i
        
        return int(bestMove)
    