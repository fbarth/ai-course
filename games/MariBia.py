import random
from Player import Player

#
# Authors: Mariana e Beatriz
#

class MariBia(Player):

    def name(self):
        return "Mari e Bia"

    def getBoardCopy(self, board):
        # Faz uma copia da lista do tabuleiro e retorna
        dupeBoard = []

        for i in board:
            dupeBoard.append(i)

        return dupeBoard

    def chooseRandomMoveFromList(self, board, movesList):
    # Retorna um movimento valido da lista passada no tabuleiro
        possibleMoves = []
        for i in movesList:
            if self.isSpaceFree(board, i):
                possibleMoves.append(i)

        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None        
    

    def move(self, player_code, board):
        # Dado um tabuleiro e o simbolo do jogador, a funcao determina onde jogar e retorna o movimento

        for i in range(0,9):
            copy = self.getBoardCopy(board)
            if self.isSpaceFree(copy, i):
               self.makeMove(copy, self, i)
               if self.isWinner(copy, self):
                   return i

        # Verifica se o jogador pode vencer na proxima jogada e, entao, o bloqueia
        for i in range(0,9):
            copy = self.getBoardCopy(board)
            #print(copy)
            if self.isSpaceFree(copy, i):
                self.makeMove(copy, player_code, i)
                if self.isWinner(copy, player_code):
                    #print('oi')
                    return i

        # Tenta ocupar algum dos cantos, se eles estiverem livres
        move = self.chooseRandomMoveFromList(board, [0, 2, 6, 8])
        if move != None:
            return move

        # Tenta ocupar o centro, se estiver livre
        if self.isSpaceFree(board, 4):
            return 4

        # Ocupa os lados
        x = self.chooseRandomMoveFromList(board, [1, 3, 5, 7])
        return x

    def isBoardFull(self, board):
         # Retorna True se todos os espacos do tabuleiro estiverem ocupados
         for i in range(0,9):
             if self.isSpaceFree(board, i):
                 return False
         return True

    def isSpaceFree(self, board, move):
        # Retorna True se a jogada esta livre no tabuleiro
        return board[move] == 0

    def makeMove(self, board, letter, move):
        board[move] = letter
    
    def isWinner(self, bo, le):
        # Esta funcao retorna True se o jogador vencer o jogo
        # Usamos bo, ao inves de board, e le, ao inves de letter, para que nao precisemos digitar tanto
        return ((bo[6] == le and bo[7] == le and bo[8] == le) or (bo[3] == le and bo[4] == le and bo[5] == le) or (bo[0] == le and bo[1] == le and bo[2] == le) or (bo[6] == le and bo[3] == le and bo[0] == le) or (bo[7] == le and bo[4] == le and bo[1] == le) or (bo[8] == le and bo[5] == le and bo[2] == le) or (bo[6] == le and bo[4] == le and bo[2] == le) or (bo[8] == le and bo[4] == le and bo[0] == le))




           


