from Player import Player
import numpy as np
from random import randint

#
# authors: Gustavo and Heitor
# date: May, 2020

class SushiPlayer(Player):

    def name(self):
        return "Sushi"

    def max_value(self, board, action, player_code, depth, alpha, beta):
        if (depth == 0):
            # retorna o valor para o estado e a acao que gerou o estado
            return self.eval(player_code, board), action
        v = -99999
        sucessores = self.sucessores(player_code, board)
        
        for s in sucessores:
            mv, ac = self.min_value(s['board'], s['action'], self.opponent(player_code), depth - 1, alpha, beta)
            
            alpha = max(alpha, mv)
            if beta <= alpha:
                break

            if (mv > v):
                v = mv
                action = ac
        return v, action
    
    def min_value(self, board, action, player_code, depth, alpha, beta):
        if (depth == 0):
            # retorna o valor para o estado e a acao que gerou o estado
            return self.eval(player_code, board), action
        v = +99999
        sucessores = self.sucessores(player_code, board)
        
        for s in sucessores:
            mv, ac = self.max_value(s['board'], s['action'], self.opponent(player_code), depth - 1, alpha, beta)
            
            beta = min(beta, mv)
            if beta <= alpha:
                break

            if (mv < v):
                v = mv
                action = ac
        return v, action

    # def isThereAnyEmergency(self, board, player_code):
    #     opponent = self.opponent(player_code)
    #     op_points_line = self.count_row_line(opponent, board)
    #     op_points_col = self.count_row_column(opponent, board)
    #     op_points_dig = self.count_row_diag(opponent, board)
    #     op_points_dig2 = self.count_row_diag(opponent, board[::-1])
        
    #     if (op_points_col['3'] > 0 or 
    #     op_points_line['3'] > 0 or 
    #     op_points_dig['3'] > 0 or 
    #     op_points_dig2['3']> 0 or 
    #     # condicoes emergenciais adiciondas
    #     op_points_line['2'] == 2 or 
    #     (op_points_line['2'] >= 1 and op_points_line['1'] >= 1)):
    #         return True
    #     return False


    def move(self, player_code, board):
        firstMove = True
        # se a coluna do meio estiver vazia depois da primeira jogada, jogar la sempre!
        if(firstMove and (board[5][3] == 0)):
            firstMove = False
            return 3
        
        #if (self.isThereAnyEmergency(board, player_code)):
        # checa se alguma jogada do oponente pode acabar com o jogo
        sucessores = self.sucessores(self.opponent(player_code), board)
        for s in sucessores:
            v = self.eval(self.opponent(player_code), s['board'])
            if (v > 70000):
                return s['action']

        # TODO qual é o maior DEPTH que podemos utilizar sem correr o risco de ultrapassar os 15s?
        _, action = self.max_value(board, None, player_code, 5, -9999999, +9999999)
        
        return action

    def sucessores(self, player_code, board):
        suc = []
        for i in range(0,7):
            b = self.movement(player_code, board, i)
            if(b is not None):
                suc.append({'board':b, 'action':i})
        return suc

    def opponent(self, player):
        if player==1:
            return 2
        return 1

    def domain_center(self, player, board):
        h = np.matrix([
            [0., 0., 0., 0., 0., 0., 0.],
            [0., 0., 0., 0., 0., 0., 0.],
            [0., 0., 1., 1., 1., 0., 0.],
            [0., 0., 1., 1., 1., 0., 0.],
            [0., 0., 1., 1., 1., 0., 0.],
            [0., 1., 1., 1., 1., 1., 0.]])   
        return np.sum(np.logical_and(board==player, h))

    def eval(self, player, board): 
        my_points_line = self.count_row_line(player, board)
        my_points_col = self.count_row_column(player, board)
        my_points_dig = self.count_row_diag(player, board)
        my_points_dig2 = self.count_row_diag(player, board[::-1])
        my_qtd_2 = my_points_line['2'] + my_points_col['2'] + my_points_dig['2'] + my_points_dig2['2']
        my_qtd_3 = my_points_line['3'] + my_points_col['3'] + my_points_dig['3'] + my_points_dig2['3']
        my_qtd_4 = my_points_line['4'] + my_points_col['4'] + my_points_dig['4'] + my_points_dig2['4']
        sum_my_points = 100000*my_qtd_4 + 100*my_qtd_3 + my_qtd_2

        opponent = self.opponent(player)
        op_points_line = self.count_row_line(opponent, board)
        op_points_col = self.count_row_column(opponent, board)
        op_points_dig = self.count_row_diag(opponent, board)
        op_points_dig2 = self.count_row_diag(opponent, board[::-1])
        op_qtd_2 = op_points_line['2'] + op_points_col['2'] + op_points_dig['2'] + op_points_dig2['2']
        op_qtd_3 = op_points_line['3'] + op_points_col['3'] + op_points_dig['3'] + op_points_dig2['3']
        op_qtd_4 = op_points_line['4'] + op_points_col['4'] + op_points_dig['4'] + op_points_dig2['4']
        sum_op_points = 100000*op_qtd_4 + 10000*op_qtd_3 + op_qtd_2
        
        #
        # TODO: explicar esta funcao de avaliacao
        #
        return sum_my_points - sum_op_points + self.domain_center(player, board)

    def count_row_line(self, player, board):
        retorno = {'2': 0, '3': 0, '4': 0}
        for i in range(6):
            counter = 0
            for j in range(6):
                if ((board[i, j] == player) and (board[i, j] == board[i, j + 1])):
                    counter = counter + 1
                else:
                    counter = 0
                if (counter==1):
                    retorno['2'] = retorno['2'] + 1
                if (counter==2):
                    retorno['3'] = retorno['3'] + 1
                if (counter==3):
                    retorno['4'] = retorno['4'] + 1
        return retorno
    
    def count_row_column(self, player, board):
        retorno = {'2': 0, '3': 0, '4': 0}
        for i in range(7):
            counter = 0
            for j in range(5):
                if ((board[j, i] == player) and (board[j, i] == board[j + 1, i])):
                    counter = counter + 1
                else:
                    counter = 0
                if (counter==1):
                    retorno['2'] = retorno['2'] + 1
                if (counter==2):
                    retorno['3'] = retorno['3'] + 1
                if (counter==3):
                    retorno['4'] = retorno['4'] + 1
        return retorno
    
    def count_row_diag(self, player, board):
        retorno = {'2': 0, '3': 0, '4': 0}
        for k in range(-2,4):
            counter = 0
            x = np.diag(board, k=k)
            for i in range(0,len(x)-1):
                if ((x[i] == player) and (x[i] == x[i+1])):
                    counter = counter + 1
                else:
                    counter = 0
                if (counter==1):
                    retorno['2'] = retorno['2'] + 1
                if (counter==2):
                    retorno['3'] = retorno['3'] + 1
                if (counter==3):
                    retorno['4'] = retorno['4'] + 1
        return retorno
  
    def movement(self, player, board, column):
        result_board = np.matrix(board)
        for i in range(5,-2,-1):
            if (board[i,column] == 0):
                break
        if(i<0):
            return None
        result_board[i, column] = player
        return result_board