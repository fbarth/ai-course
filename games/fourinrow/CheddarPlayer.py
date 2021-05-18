from Player import Player
from random import randint
import numpy as np
import math

#
# authors: Cesar
# date: May, 2020

class CheddarPlayer(Player):
    WIDTH = 7
    HEIGHT = 6
    opponent_code = None
    player_code = None
    def move(self, player_code, board):
        if player_code == 1: 
            self.opponent_code = 2
            self.player_code = player_code
        elif player_code == 2: 
            self.opponent_code = 1
            self.player_code = player_code

        _ , move = self.maxValue(board, None, -999999, 999999, 6)
        
        if self.isThereAnyEmergencies(board):
            suc = self.successors(self.opponent_code, board)
            for i in suc:
                v = self.evaluator(board)
                if v < 70000:
                    return i['op']
        return move
    
   


    def successors(self, player_code, board):
        suc = []
        b = None
        for i in range(0, 7):
            b = self.movement(player_code, board, i)
            if(b is not None):
                suc.append({'suc':b, 'op':i})
        return suc


    def movement(self, player, board, column):
        result_board = np.matrix(board)
        for i in range(5,-2,-1):
            if (board[i,column] == 0):
                break
        if(i<0):
            return None
        result_board[i, column] = player
        return result_board
    
    def evaluator(self, state):
        my_score = 0
        opponent_score = 0
        my_qtd_strikes = self.strikes(self.player_code, state)

        my_score = 1000000 * my_qtd_strikes['4'] + 10000 * my_qtd_strikes['3'] + 5 * my_qtd_strikes['2'] - my_qtd_strikes['block_score']
        
        op_qtd_strikes = self.strikes(self.opponent_code, state)
        opponent_score = 1000000 * op_qtd_strikes['4'] + 10000 * op_qtd_strikes['3'] + op_qtd_strikes['2'] + my_qtd_strikes['block_score']
        
        return my_score - opponent_score + self.domain_center(self.player_code, state)
                

    def strikes(self, player, board):
        result = {'2': 0, '3': 0, '4': 0, 'block_score': 0}
        if player == 1:
            opposing_player = 2
        elif player == 2:
            opposing_player = 1
        inverted_board = board[::-1]
        for i in range(self.HEIGHT):
            counter = 0
            #Horizontal
            for j in range(self.HEIGHT):
                if(board[i, j] == player) and (board[i, j] == board[i, j + 1]):
                    counter += 1
                else:
                    counter = 0
                if counter == 1:
                    result['2'] += 1
                    if (j + 2 < self.WIDTH and board[i, j + 2] == opposing_player) or (j - 1 >= 0 and board[i, j - 1] == opposing_player ):
                        result['block_score'] += 100
                if counter == 2:
                    result['3'] += 1
                    if (j + 2 < self.WIDTH and board[i, j + 2] == opposing_player) or (j - 2 >= 0 and board[i, j - 2] == opposing_player):
                        result['block_score'] += 100
                if counter == 3:
                    result['4'] += 1
                    if (j + 2 < self.WIDTH and board[i, j + 2] == opposing_player) or (j - 3 >= 0 and board[i, j - 3] == opposing_player):
                        result['block_score'] += 500
        for w in range(self.HEIGHT):
            counter = 0
            #Vertical 
            for b in range(5):
                if (board[b, w] == player) and (board[b, w] == board[b + 1, w]):
                    counter += 1
                else: 
                    counter = 0
                if counter == 1:
                    result['2'] += 1
                    if (w + 2 < self.HEIGHT and board[b, w + 2] == opposing_player) or (w - 1 >= 0 and board[b, w - 1] == opposing_player):
                        result['block_score'] += 100
                if counter == 2:
                    result['3'] += 1
                    if (w + 2 < self.HEIGHT and board[b, w + 2] == opposing_player) or (w - 2 >= 0 and board[b, w - 2] == opposing_player):
                        result['block_score'] += 100
                if counter == 3:
                    result['4'] += 1
                    if (w + 2 < self.HEIGHT and board[b, w + 2] == opposing_player) or (w - 1 >= 0 and board[b, w - 3] == opposing_player):
                        result['block_score'] += 500
        #Diagonal
        for l in range(-2, 3):
            counter = 0
            x = np.diag(board, k = l)
            capacity = len(x) - 1
            for i in range(capacity):
                if (x[l] == player) and (x[l] == x[l + 1]):
                    counter += 1
                else:
                    counter = 0
                if counter == 1:
                    result['2'] += 1
                    if (i + 2 < capacity and x[i + 2] == opposing_player) or (i - 1 >= 0 and x[i - 1] == opposing_player):
                        result['block_score'] += 10
                if counter == 2:
                    result['3'] += 1
                    if (i + 2 < capacity and x[i + 2] == opposing_player) or (i - 2 >= 0 and x[i - 2] == opposing_player):
                        result['block_score'] += 100
                if counter == 3:
                    result['4'] += 1
                    if (i + 2 < capacity and x[i + 2] == opposing_player) or (i - 3 >= 0 and x[i - 3] == opposing_player):
                        result['block_score'] += 500
        # Inverted Diagonal
        for p in range(-2, 3):
            counter = 0
            x = np.diag(inverted_board, k = p)
            for i in range(0, len(x) - 1):
                if (x[i] == player) and (x[i] == x[i + 1]):
                    counter += 1
                else:
                    counter = 0
                if counter == 1:
                    result['2'] += 1
                    if (i + 2 < capacity and x[i + 2] == opposing_player) or (i - 1 >= 0 and x[i - 1] == opposing_player):
                        result['block_score'] += 10
                if counter == 2:
                    result['3'] += 1
                    if (i + 2 < capacity and x[i + 2] == opposing_player) or (i - 2 >= 0 and x[i - 2] == opposing_player):
                        result['block_score'] += 100
                if counter == 3:
                    result['4'] += 1
                    if (i + 2 < capacity and x[i + 2] == opposing_player) or (i - 3 >= 0 and x[i - 3] == opposing_player):
                        result['block_score'] += 500
        return result

    def domain_center(self, player, board):
        h = np.matrix([
            [0., 0., 0., 0., 0., 0., 0.],
            [0., 0., 0., 0., 0., 0., 0.],
            [0., 0., 1., 1., 1., 0., 0.],
            [0., 0., 1., 1., 1., 0., 0.],
            [0., 0., 1., 1., 1., 0., 0.],
            [0., 1., 1., 1., 1., 1., 0.]])
        
        return np.sum(np.logical_and(board == player, h))
    
    def isThereAnyEmergencies(self, board):
        op_strikes = self.strikes(self.opponent_code, board)
        if(op_strikes['3'] > 0):
            return True
        return False
        
    def maxValue(self, state, action, alpha, beta, p):
        if p == 0:
            return self.evaluator(state), action
        for s in self.successors(self.player_code, state):
            mv, ac = self.minValue(s['suc'], s['op'], alpha, beta, p - 1)
            if mv > alpha:
                alpha = mv
                action = ac
            if alpha >= beta:
                return alpha, action
        return alpha, action
    
    def minValue(self, state, action, alpha, beta, p):
        if p == 0:
            return self.evaluator(state), action
        for s in self.successors(self.opponent_code, state):
            mv, ac = self.maxValue(s['suc'], s['op'], alpha, beta, p - 1)
            if mv < beta:
                beta = mv
                action = ac
            if beta <= alpha:
                return beta, action
        return beta, action
    
    def name(self):
        return "Cheddar Player"

    
        

