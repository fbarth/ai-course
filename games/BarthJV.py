from numpy import mat
from Player import Player
import math
#
# uma versao de jogador do jogo da velha
# usando min-max com uma funcao de avaliacao considerando
# estados terminais
#

class BarthJV(Player):

    def opponent(self, player_code):
        if player_code == 1:
            return 2
        else:
            return 1

    def eval(self, player_code, board):
        #
        # como o espaco de busca eh pequeno, vou colocar
        # apenas regras para calcular o valor de estados finais
        #
        #m = [1,0,1,0,3,0,1,0,1]

        if((board[0] == board[1] == board[2]) & (board[0] != 0)):
            if (board[0] == player_code):
                return 10
            else:
                return -10
        elif((board[3] == board[4] == board[5]) & (board[3] != 0)):
            if (board[3] == player_code):
                return 10
            else:
                return -10
        elif((board[6] == board[7] == board[8]) & (board[6] != 0)):
            if (board[6] == player_code):
                return 10
            else:
                return -10
        elif((board[0] == board[3] == board[6]) & (board[0] != 0)):
            if (board[0] == player_code):
                return 10
            else:
                return -10
        elif((board[1] == board[4] == board[7]) & (board[1] != 0)):
            if (board[1] == player_code):
                return 10
            else:
                return -10
        elif((board[2] == board[5] == board[8]) & (board[2] != 0)):
            if (board[2] == player_code):
                return 10
            else:
                return -10
        elif((board[0] == board[4] == board[8]) & (board[0] != 0)):
            if (board[0] == player_code):
                return 10
            else:
                return -10
        elif((board[2] == board[4] == board[6]) & (board[2] != 0)):
            if (board[2] == player_code):
                return 10
            else:
                return -10
        else:
            return 0

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

    
    def isLine(self, b1, b2, b3):
        if (b1 == b2) & (b1 != 0) & (b3 ==0):
            return True
        elif (b2 == b3) & (b2 != 0) & (b1==0):
            return True
        elif (b1 == b3) & (b1 != 0) & (b2==0):
            return True
        else:
            return False
    
    def mustPlay(self, board):
        #
        # se existe uma condicao de ganho ou perda eminente 
        # entao jogar na posicao informada. se a funcao retornar
        # 9 entao nao jogar
        #
        if(self.isLine(board[0],board[1],board[2])):
            if board[0]==0:
                return 0
            elif board[1]==0:
                return 1
            elif board[2]==0:
                return 2
        elif(self.isLine(board[3],board[4],board[5])):
            if board[3]==0:
                return 3
            elif board[4]==0:
                return 4
            elif board[5]==0:
                return 5
        elif(self.isLine(board[6],board[7],board[8])):
            if board[6]==0:
                return 6
            elif board[7]==0:
                return 7
            elif board[8]==0:
                return 8
        elif(self.isLine(board[0],board[3],board[6])):
            if board[0]==0:
                return 0
            elif board[3]==0:
                return 3
            elif board[6]==0:
                return 6
        elif(self.isLine(board[1],board[4],board[7])):
            if board[1]==0:
                return 1
            elif board[4]==0:
                return 4
            elif board[7]==0:
                return 7
        elif(self.isLine(board[2],board[5],board[8])):
            if board[2]==0:
                return 2
            elif board[5]==0:
                return 5
            elif board[8]==0:
                return 8
        elif(self.isLine(board[0],board[4],board[8])):
            if board[0]==0:
                return 0
            elif board[4]==0:
                return 4
            elif board[8]==0:
                return 8
        elif(self.isLine(board[2],board[4],board[6])):
            if board[2]==0:
                return 2
            elif board[4]==0:
                return 4
            elif board[6]==0:
                return 6
        else:
            return 9

    def isBoardFull(self, board):
        for i in range(9):
            if board[i] == 0:
                return False
        return True
    
    def isEmpty(self, board):
        for i in range(9):
            if board[i] != 0:
                return False
        return True

    def sucessores(self, player_code, board):
        boards = []
        for i in range(9):
            if board[i] == 0:
                x = board.copy()
                x[i] = player_code
                boards.append([i,x])    
        return boards

    def max_value(self, player_code, board, action):
        if (self.isBoardFull(board) or self.hasWinner(board)):
            temp = self.eval(player_code,board)
            return action, temp
        value = -math.inf
        for [i,s] in self.sucessores(player_code, board):
            s_filho = s.copy()
            action, new = self.min_value(player_code, s_filho, i)
            if new > value:
                value = new
                action = action
        return action, value
    
    def min_value(self, player_code, board, action):
        if (self.isBoardFull(board) or self.hasWinner(board)):
            temp = self.eval(player_code,board)
            return action, temp
        
        value = math.inf
        opponent = self.opponent(player_code)
        for [i,s] in self.sucessores(opponent, board):
            s_filho = s.copy()
            action, new = self.max_value(player_code, s_filho, i)
            if new < value:
                value = new
                action = action
        return action, value

    def move(self, player_code, board):
        x = self.mustPlay(board)
        if x != 9:
            return x
        elif self.isEmpty(board):
            return 4
        else:
            action, value = self.max_value(player_code, board, None)
            return action
    
    def name(self):
        return "Barth JV"