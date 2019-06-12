from SearchAlgorithms import SubidaMontanhaEnzo
from Graph import State
from random import randrange

# projeto falho de Enzo Scapinelli

class N_Queens(State):

    def __init__(self, board):
        self.board = board
    
    def sucessors(self):
        sucessors = []
        next_state = self.board
        queen = self.queen_Place()

        for x in range(len(self.board)):
            line_number = x
            next_state[line_number][queen] = 0

            if (queen < len(self.board) and self.is_not_Safe):
                next_state[line_number][queen+1] = 1
            if (queen > 0 and self.is_not_Safe):
                next_state[line_number][queen-1] = 1
  
        sucessors.append(N_Queens(next_state))
        return sucessors


    def is_goal(self):
        h = 0
        for x in range(len(self.board)):
            queen_y = self.board[x].index(1)
            for x in range(len(self.board)):
                if self.board[x][queen_y] == 1:
                    h = h + 1
        
        if h > 1:
            return False
        else:
            return True
    
    def is_not_Safe(self, x):
        for x in range(len(self.board)):
            queen_y = self.board[x].index(1)
            h = 0
            for x in range(len(self.board)):
                if self.board[x][queen_y] == 1:
                    h = h + 1
        if h > 1:
            return True
        else:
            return False
        
    
    def description(self):
        return "N-Queens problem"
    
    def cost(self):
        return 1

    def print(self):
        pass

    def printEnv(self):
        return self.board
    
    def queen_Place(self):
        for x in range(len(self.board)):
            queen_y = self.board[x].index(1)
            for x in range(len(self.board)):
                if self.board[x][queen_y] == 1:
                    return x
            
        return h

    def h(self):
        h = 0
        for x in range(len(self.board)):
            queen_y = self.board[x].index(1)
            for x in range(len(self.board)):
                if self.board[x][queen_y] == 1:
                    h = h + 1

            
        return h


def main():
    print('Hill-climbing Algorithm')

    n = 4
    board = [[0 for x in range(n)] for y in range(n)]
    for x in range(n):
        board[x][0] = 1
    # board[0][0] = 1
    # board[1][1] = 1
    # board[2][2] = 1
    # board[3][3] = 1

    state = N_Queens(board)
    algorithm = SubidaMontanhaEnzo()
    result = algorithm.search(state)
    if result != None and n > 3:
        print('Achou!')
        print(result.printEnv())
    else:
        if n <4 or n > 10:
            print('n fora do padrão')
        print('Nao achou solucao')

if __name__ == '__main__':
	main()
