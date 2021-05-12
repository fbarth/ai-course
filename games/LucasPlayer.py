from Player import Player
import numpy as np

#
# Author: Lucas Ciola
#

class BiggerBrainBot(Player):

    def name(self):
        return 'BiggerBrainBot'
    
    def move(self, player_code, board):
        bestScore = float('-inf')
        bestMove = 0

        for i in range(0, 9):
            if(board[int(i)] == 0):
                board[int(i)] = player_code
                score = self.minimax(board, 0, False, player_code)
                board[i] = 0
                if (score > bestScore):
                    bestScore = score
                    bestMove = i
        
        return bestMove

    def checkWin(self, board):
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

    def checkPlayerWin(self, board, code):
        if board[0] == board[1] and board[0] == board[2] and board[0] == code:
            return True
        elif (board[3] == board[4] and board[3] == board[5] and board[3] == code):
            return True
        elif (board[6] == board[7] and board[6] == board[8] and board[6] == code):
            return True
        elif (board[0] == board[3] and board[0] == board[6] and board[0] == code):
            return True
        elif (board[1] == board[4] and board[1] == board[7] and board[1] == code):
            return True
        elif (board[2] == board[5] and board[2] == board[8] and board[2] == code):
            return True
        elif (board[0] == board[4] and board[0] == board[8] and board[0] == code):
            return True
        elif (board[6] == board[4] and board[6] == board[2] and board[6] == code):
            return True
        else:
            return False

    def isDraw(self, board):
        for i in range(0,9):
            if board[i] == 0:
                return False
        if self.checkWin(board):
            return False
        else:
            return True

    def invertCode(self, player_code):
        if player_code == 1:
            return 2
        if player_code == 2:
            return 1

    def minimax(self, board, depth, isMaximizing, player_code):
        if self.checkPlayerWin(board, player_code):
            return 10
        elif self.checkPlayerWin(board, self.invertCode(player_code)):
            return -10
        elif self.isDraw(board):
            return 0

        if isMaximizing:
            bestScore = float('-inf')

            for i in range(0,9):
                if(board[i] == 0):
                    board[i] = player_code
                    score = self.minimax(board, 0, False, player_code)
                    board[i] = 0
                    if (score > bestScore):
                        bestScore = score
            return bestScore

        else:
            bestScore = float('inf')

            for i in range(0,9):
                if(board[i] == 0):
                    board[i] = self.invertCode(player_code)
                    score = self.minimax(board, 0, True, player_code)
                    board[i] = 0
                    if (score < bestScore):
                        bestScore = score
            return bestScore

