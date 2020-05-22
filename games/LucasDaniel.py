from Player import Player
import numpy as np
import random
import sys
import math


class LucasDaniel(Player):

    def move(self, player_code, board):
        #
        # O jogador sabe qual é o seu número (player_code)
        # e consegue visualizar o ambiente (tabuleiro) através da variável board.
        #
        # A implementação deste método deve identificar qual é a melhor jogada que o
        # jogador deve fazer com o objetivo de ganhar o jogo
        #
        # O método sempre deve retornar um valor entre 0 e 6 - que significa o número
        # da coluna onde ele deverá jogar.
        #
        # Além disso, não pode escolher uma coluna que já esteja completa.
        #
        col, _ = self.minimax(board, 5, True, player_code, -math.inf, math.inf)

        return col

    def goal(self, board, player_code):
        opp_player_code = 1

        if player_code == 1:
            opp_player_code = 2
        
        return self.endOfGame(board, player_code) or self.endOfGame(board, opp_player_code) or len(self.get_canPlay(board)) == 0

    def canPlay(self, board, col):
        # Ver se a ultima linha está preenchida
        return board[0][col] == 0

    def get_canPlay(self, board):
        # Transforma a resposta do canPlay em Array
        loc = []
        for col in range(7):
            if self.canPlay(board, col):
                loc.append(col)
        return loc

    def score_p(self, board, player_code):
        score = 0

        # favorecer jogadas no centro
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
        opp_player_code = 1

        if player_code == 1:
            opp_player_code = 2

        if gap.count(player_code) == 4:
            score += 1000
        elif gap.count(player_code) == 3 and gap.count(0) == 1:
            score += 6
        elif gap.count(player_code) == 2 and gap.count(0) == 2:
            score += 3

        if gap.count(opp_player_code) == 3 and gap.count(0) == 1:
            score -= 5
        elif gap.count(opp_player_code) == 2 and gap.count(0) == 2:
            score -= 2

        return score

    def next_row(self, board, col):
        # Mostra quais as linhas disponiveis
        for r in range(5, -1, -1):
            if board[r][col] == 0:
                return r

    def minimax(self, board, depth, maxminP, player_code, alfa, beta):
        valid_locations = self.get_canPlay(board)
        x_goal = self.goal(board, player_code)
        
        if player_code == 1:
            opp_player_code = 2
        else:
            opp_player_code = 1
        
        if depth == 0 or x_goal:
            if x_goal:
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
                n_score = self.minimax(c_board, depth-1, False, player_code, alfa, beta)[1]
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
                n_score = self.minimax(c_board, depth-1, True, player_code, alfa, beta)[1]
                if n_score < value:
                    value = n_score
                    column = col
                beta = min(beta, value)
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

    def name(self):
        return "Daniel/Lucas"