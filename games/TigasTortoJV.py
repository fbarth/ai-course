from Player import Player
import numpy as np

#
# Authors: Thiago Rossi e Heitor
#

class TigasTorto(Player):

    def name(self):
        return 'Tigas e Torto'

    def hasWinner(self, board):
        if((board[0] == board[1] == board[2]) & (board[0] != 0)):
            return True
        elif((board[3] == board[4] == board[5]) & (board[3] != 0)):
            return True
        elif((board[6] == board[7] == board[8]) & (board[6] != 0)):
            return True
        elif((board[0] == board[3] == board[6]) & (board[0] != 0)):
            return True
        elif((board[1] == board[4] == board[7]) & (board[1] != 0)):
            return True
        elif((board[2] == board[5] == board[8]) & (board[2] != 0)):
            return True
        elif((board[0] == board[4] == board[8]) & (board[0] != 0)):
            return True
        elif((board[2] == board[4] == board[6]) & (board[2] != 0)):
            return True
        else:
            return False

    def checkForWin(self, board, player):
        if board[0] == board[1] and board[0] == board[2] and board[0] == player:
            return True
        elif (board[3] == board[4] and board[3] == board[5] and board[3] == player):
            return True
        elif (board[6] == board[7] and board[6] == board[8] and board[6] == player):
            return True
        elif (board[0] == board[3] and board[0] == board[6] and board[0] == player):
            return True
        elif (board[1] == board[4] and board[1] == board[7] and board[1] == player):
            return True
        elif (board[2] == board[5] and board[2] == board[8] and board[2] == player):
            return True
        elif (board[0] == board[4] and board[0] == board[8] and board[0] == player):
            return True
        elif (board[6] == board[4] and board[6] == board[2] and board[6] == player):
            return True
        else:
            return False

    def checkForDraw(self, board):
        for i in range(0,9):
            if board[i] == 0:
                return False
        if self.hasWinner(board):
            return False
        else:
            return True

    def opponent(self, player_code):
        if player_code == 1:
            return 2
        if player_code == 2:
            return 1

    def minimax(self, board, p, isMax, player_code):
        if self.checkForWin(board, player_code):
            return 100
        elif self.checkForWin(board, self.opponent(player_code)):
            return -100
        elif self.checkForDraw(board):
            return 0

        if isMax:
            bestScore = -9999

            for i in range(0,9):
                if(board[i] == 0):
                    board[i] = player_code
                    score = self.minimax(board, 0, False, player_code)
                    board[i] = 0
                    if (score > bestScore):
                        bestScore = score
            return int(bestScore)

        else:
            bestScore = 9999

            for i in range(0,9):
                if(board[i] == 0):
                    board[i] = self.opponent(player_code)
                    score = self.minimax(board, 0, True, player_code)
                    board[i] = 0
                    if (score < bestScore):
                        bestScore = score
            return int(bestScore)

    def move(self, player_code, board):
        bestScore = -9999
        bestMove = 0

        for i in range(0, 9):
            if(board[int(i)] == 0):
                board[int(i)] = player_code
                score = self.minimax(board,0,False,player_code)
                board[i] = 0
                if (score > bestScore):
                    bestScore = score
                    bestMove = i
        
        return int(bestMove)
    