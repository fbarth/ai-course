from Player import Player
import numpy as np
import sys
import math
import random

#
# authors: Bruna and Jose
# date: May, 2020

class Bru_Jose(Player):

    def name(self):
        return "Bru_Jose"

    def move(self, player_code, board):

        col, _ = self.minimax(board, 1, True, player_code, -math.inf, math.inf)

        return col

    def goal(self, board, player_code):
        if player_code == 1:
            opp_player_code = 2
        else:
            opp_player_code = 1
        return self.endOfGame(board, player_code) or self.endOfGame(board, opp_player_code) or self.get_Cplay(board) == 0

    def Cplay(self, board, col):
        # Consegue devolver a resposta do jogo e se ela esta preenchida
        return board[0][col] == 0

    def get_Cplay(self, board):
        # Cplay em Array
        loc = []
        for col in range(7):
            if self. Cplay(board, col):
                loc.append(col)
        return loc

    def score_p(self, board, player_code):
        score = 0

        # Cria uma heuristica

        # Jogadas localizadas no centro do tabuleiro
        a_center = [int(i) for i in list(board[:, 3])]
        n_center = a_center.count(player_code)
        score += n_center * 3
        
        # Horizontal
        for r in range(6):
            a_row = [int(i) for i in list(board[r, :])]
            for v in range(4):
                gap = a_row[v:v+4]
                score += self.ev_gap(gap, player_code)

        # Vertical
        for c in range(7):
            a_col = [int(i) for i in list(board[:, c])]
            for v in range(3):
                gap = a_col[v:v+4]
                score += self.ev_gap(gap, player_code)

        # Diagonal /
        for r in range(3):
            for c in range(4):
                gap = [board[r+i][c+i] for i in range(4)]
                score += self.ev_gap(gap, player_code)

        # Diagonal \
        for r in range(3):
            for c in range(4):
                gap = [board[r+3-i][c+i] for i in range(4)]
                score += self.ev_gap(gap, player_code)

        return score

    def ev_gap(self, gap, player_code):
        score = 0

        if player_code == 1:
            opp_player_code = 2
        else:
            opp_player_code = 1

        if gap.count(player_code) == 4:
            score += 100
        elif gap.count(player_code) == 3 and gap.count(0) == 1:
            score += 6
        elif gap.count(player_code) == 2 and gap.count(0) == 2:
            score += 3

        if gap.count(opp_player_code) == 3 and gap.count(0) == 1:
            score -= 5

        return score

    def next_row(self, board, col):
        # Linhas disponiveis
        for r in range(5, -1, -1):
            if board[r][col] == 0:
                return r

    def minimax(self, board, depth, maxminP, player_code, alfa, beta):
        valid_locations = self.get_Cplay(board)
        x_goal = self.goal(board, player_code)
        if player_code == 1:
            opp_player_code = 2
        else:
            opp_player_code = 1
        if depth == 0 or x_goal:
            if self.goal(board, player_code):
                if self.endOfGame(board, player_code):
                    return (None, 99999999)
                elif self.endOfGame(board, opp_player_code):
                    return(None, -999999999)
                else:
                    return (None, 0)
            else:
                return (None, self.score_p(board, player_code))
        if maxminP:
            column = random.choice(valid_locations)
            value = -math.inf
            for col in valid_locations:
                r = self.next_row(board, col)
                c_board = board.copy()
                self.doAPlay(c_board, r, col, player_code)
                n_score = self.minimax(
                    c_board, depth-1, False, player_code, alfa, beta)[1]
                if n_score > value:
                    value = n_score
                    column = col
                alfa = max(alfa, value)
                if alfa >= beta:
                    break
            return column, value
        else:
            value = math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                r = self.next_row(board, col)
                c_board = board.copy()
                self.doAPlay(c_board, r, col, opp_player_code)
                n_score = self.minimax(
                    c_board, depth-1, True, player_code, alfa, beta)[1]
                if n_score < value:
                    value = n_score
                    column = col
                alfa = min(beta, value)
                if alfa >= beta:
                    break
            return column, value

    def endOfGame(self, board, player_code):
        # Horizontal
        for c in range(4):
            for r in range(6):
                if board[r][c] == player_code and board[r][c+1] == player_code and board[r][c+2] == player_code and board[r][c+3] == player_code:
                    return True

        # Vertical
        for c in range(7):
            for r in range(3):
                if board[r][c] == player_code and board[r+1][c] == player_code and board[r+2][c] == player_code and board[r+3][c] == player_code:
                    return True

        # Diagonal /
        for c in range(4):
            for r in range(3):
                if board[r][c] == player_code and board[r+1][c+1] == player_code and board[r+2][c+2] == player_code and board[r+3][c+3] == player_code:
                    return True

        # Diagonal \
        for c in range(4):
            for r in range(3, 6):
                if board[r][c] == player_code and board[r-1][c+1] == player_code and board[r-2][c+2] == player_code and board[r-3][c+3] == player_code:
                    return True

    def doAPlay(self, board, row, col, player_code):
        board[row][col] = player_code
