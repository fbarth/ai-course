from Player import Player
import numpy as np
from random import randint

#
# Authors: Henrique, Matheus e Luigi
# 

class AstolfoPlayer(Player):

    def name(self):
        # TODO alterar o nome da classe, do arquivo e do retorno deste método
        return "Astolfo"


    def max_value(self, board, action, player_code, p):
        if (p==0):
            # retorna o valor para o estado e a acao que gerou o estado (Done)
            return self.eval(player_code, board), action
        v = -99999
        sucessores = self.sucessores(board)#TODO executar o metodo sucessores(DONE)
        for s in sucessores:
            mv, ac = self.min_value(s['board'], s['action'], player_code, p-1) #TODO executar o metodo min_value (DONE)
            if (mv > v):
                v = mv
                action = ac
        return v, action
    

    def min_value(self, board, action, player_code, p):
        if (p==0):
            # retorna o valor para o estado e a acao que gerou o estado (Done)
            return self.eval(player_code, board), action
        v = 99999
        sucessores = self.sucessores(board)#TODO executar o metodo sucessores(DONE)
        for s in sucessores:
            mv, ac = self.max_value(s['board'], s['action'], player_code, p-1) #TODO executar o metodo min_value (DONE)
            if (mv < v):
                v = mv
                action = ac
        return v, action


    def move(self, player_code, board):
        # TODO qual é o maior p que podemos utilizar sem correr o
        # risco de ultrapassar os 15s? 
        _, action = self.max_value(board, None, player_code, 3)
        return action


    def sucessores(self, board):
        suc = []
        for i in range(0,7):
            if(board[i] == 0):
                suc.append({'board':board, 'action':i})
        return suc


    def opponent(self, player):
        if player==1:
            return 2
        return 1


    def eval(self, player, board):
        # Retornar 1 se ganhar, retornar -1 se tiver perdido e 0 se ainda não tiver ganhado e nem perdido
        if hasWinner(board, player):
            return 100
        elif hasWinner(board, self.opponent(player)):
            return -100
        else:
            return 0


def hasWinner(board, player_code):
    if((board[0] == board[1] == board[2]) & (board[0] == player_code)):
        return True
    elif((board[3] == board[4] == board[5]) & (board[3] == player_code)):
        return True
    elif((board[6] == board[7] == board[8]) & (board[6] == player_code)):
        return True
    elif((board[0] == board[3] == board[6]) & (board[0] == player_code)):
        return True
    elif((board[1] == board[4] == board[7]) & (board[1] == player_code)):
        return True
    elif((board[2] == board[5] == board[8]) & (board[2] == player_code)):
        return True
    elif((board[0] == board[4] == board[8]) & (board[0] == player_code)):
        return True
    elif((board[2] == board[4] == board[6]) & (board[2] == player_code)):
        return True
    else:
        return False