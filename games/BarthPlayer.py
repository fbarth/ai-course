from Player import Player

class PlayerSpecification(Player):

    def move(self, player_code, board):
        sucessores = self.sucessores(player_code, board)
        # for each sucessor in sucessores calcular o eval
        return None

    def sucessores(self, player_code, board):
        suc = []
        for i in range(0,7):
            b = self.movement(player_code, board, i)
            if(b != None):
                suc.append(b)
        return suc

    def eval(self, board):
        # se o meu oponente tem quatro em uma linha entao -100000
        # senao 100000*(#4-in-row) + 100*(#3-in-row) + (#2-in-row)
        return None
    
    def movement(self, player, board, column):
        result_board = board
        for i in range(5,-2,-1):
            if (board[i,column] == 0):
                break
        if(i<0):
            return None
        result_board[i, column] = player
        return result_board

